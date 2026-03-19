# =============================================================================
# Deep Learning Tingkat Mahir – Zahri Ramadhani
# Multi-Step Time Series Forecasting (24-step) dengan Bitcoin OHLCV Data
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 0 – Import Library
# ─────────────────────────────────────────────────────────────────────────────
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")          # non-interactive backend agar plot disimpan ke file
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import warnings
warnings.filterwarnings("ignore")

# Reproducibility
tf.random.set_seed(42)
np.random.seed(42)

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("  Deep Learning Tingkat Mahir – Zahri Ramadhani")
print("=" * 60)
print(f"TensorFlow version : {tf.__version__}")
print(f"Output directory   : {OUTPUT_DIR}\n")

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 1 – Load & Inspect Data
# ─────────────────────────────────────────────────────────────────────────────
print("\n[1/14] Load & Inspect Data")
print("-" * 40)

DATA_PATH = os.path.join(OUTPUT_DIR, "Bitcoin3.csv")
df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
df = df.sort_values("Date").reset_index(drop=True)

# Pilih fitur (minimal 3 sesuai kriteria; kita pakai 6)
FEATURES = ["Close", "Volume USDT", "RSI", "MACD_Hist", "ATR", "KAMAO"]
TARGET   = "Close"

print(f"Shape awal  : {df.shape}")
print(f"Rentang waktu: {df['Date'].min()} → {df['Date'].max()}")
print(f"Fitur digunakan: {FEATURES}")
print(df[FEATURES].head())
print("\nMissing values:\n", df[FEATURES].isnull().sum())

# Drop baris yang memiliki NaN pada fitur yang digunakan
df = df.dropna(subset=FEATURES).reset_index(drop=True)
print(f"Shape setelah dropna: {df.shape}")

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 2 – EDA: Heatmap Korelasi (Kriteria 1)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[2/14] EDA – Heatmap Korelasi")
print("-" * 40)

fig, ax = plt.subplots(figsize=(9, 7))
corr_matrix = df[FEATURES].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    square=True,
    ax=ax,
    vmin=-1, vmax=1,
)
ax.set_title("Heatmap Korelasi Antar Fitur", fontsize=14, fontweight="bold", pad=15)
plt.tight_layout()
heatmap_path = os.path.join(OUTPUT_DIR, "heatmap_korelasi.png")
plt.savefig(heatmap_path, dpi=120)
plt.close()
print(f"  → Disimpan: {heatmap_path}")

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 3 – ACF & PACF untuk Menentukan Window Size (Kriteria 1 – Advanced)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[3/14] Analisis ACF & PACF")
print("-" * 40)

close_series = df[TARGET].values
N_LAGS = 100

fig, axes = plt.subplots(2, 1, figsize=(14, 8))
plot_acf(close_series,  lags=N_LAGS, ax=axes[0], alpha=0.05)
axes[0].set_title("ACF – Close Price (Bitcoin)", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Lag (jam)", fontsize=11)

plot_pacf(close_series, lags=N_LAGS, ax=axes[1], alpha=0.05, method="ywm")
axes[1].set_title("PACF – Close Price (Bitcoin)", fontsize=13, fontweight="bold")
axes[1].set_xlabel("Lag (jam)", fontsize=11)

plt.tight_layout()
acf_path = os.path.join(OUTPUT_DIR, "acf_pacf.png")
plt.savefig(acf_path, dpi=120)
plt.close()
print(f"  → Disimpan: {acf_path}")

# Berdasarkan PACF: lag signifikan terlihat hingga ~48 jam (2 hari)
WINDOW_SIZE      = 48
FORECAST_HORIZON = 24

print(f"  Window size dipilih : {WINDOW_SIZE} jam (berdasarkan PACF)")
print(f"  Forecast horizon    : {FORECAST_HORIZON} step ke depan")

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 4 – Feature Engineering: Rolling Statistics (Kriteria 1 – Advanced)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[4/14] Feature Engineering – Rolling Statistics")
print("-" * 40)

ROLL_W = 24   # rolling window 24 jam (1 hari)

df["Close_RollMean"] = df["Close"].rolling(window=ROLL_W).mean()
df["Close_RollStd"]  = df["Close"].rolling(window=ROLL_W).std()
df["Close_RollMin"]  = df["Close"].rolling(window=ROLL_W).min()
df["Close_RollMax"]  = df["Close"].rolling(window=ROLL_W).max()

# Tambahkan fitur rolling ke daftar fitur
FEATURES_EXT = FEATURES + [
    "Close_RollMean", "Close_RollStd", "Close_RollMin", "Close_RollMax"
]

# Drop NaN hasil rolling
df = df.dropna(subset=FEATURES_EXT).reset_index(drop=True)
print(f"  Fitur setelah rolling : {FEATURES_EXT}")
print(f"  Shape setelah rolling : {df.shape}")

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 5 – Split Data 70/15/15 & Normalisasi (Tanpa Data Leakage)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[5/14] Split & Normalisasi Data")
print("-" * 40)

data_arr = df[FEATURES_EXT].values   # shape: (N, n_features)
N = len(data_arr)

train_end = int(N * 0.70)
val_end   = int(N * 0.85)

train_data = data_arr[:train_end]
val_data   = data_arr[train_end:val_end]
test_data  = data_arr[val_end:]

print(f"  Train : {len(train_data):>6} baris  ({train_end}/{N} = 70%)")
print(f"  Val   : {len(val_data):>6} baris  ({val_end - train_end}/{N} = 15%)")
print(f"  Test  : {len(test_data):>6} baris  ({N - val_end}/{N} = 15%)")

# Fit scaler HANYA pada training set → tidak ada data leakage
scaler = MinMaxScaler(feature_range=(0, 1))
train_scaled = scaler.fit_transform(train_data)
val_scaled   = scaler.transform(val_data)
test_scaled  = scaler.transform(test_data)

# Indeks kolom target (Close) untuk inverse transform nanti
TARGET_IDX = FEATURES_EXT.index(TARGET)   # 0
print(f"  Target column index : {TARGET_IDX} ({TARGET})")

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 6 – Buat Sliding Window Dataset
# ─────────────────────────────────────────────────────────────────────────────
print("\n[6/14] Membuat Dataset Sliding Window")
print("-" * 40)

def create_sequences(data, window_size, forecast_horizon):
    """
    Parameter
    ---------
    data            : ndarray (timesteps, n_features), sudah di-scale
    window_size     : jumlah step input
    forecast_horizon: jumlah step prediksi ke depan

    Return
    ------
    X : ndarray (samples, window_size, n_features)
    y : ndarray (samples, forecast_horizon)  ← hanya kolom Close (index 0)
    """
    X, y = [], []
    for i in range(len(data) - window_size - forecast_horizon + 1):
        X.append(data[i : i + window_size])
        y.append(data[i + window_size : i + window_size + forecast_horizon, TARGET_IDX])
    return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)

X_train, y_train = create_sequences(train_scaled, WINDOW_SIZE, FORECAST_HORIZON)
X_val,   y_val   = create_sequences(val_scaled,   WINDOW_SIZE, FORECAST_HORIZON)
X_test,  y_test  = create_sequences(test_scaled,  WINDOW_SIZE, FORECAST_HORIZON)

print(f"  X_train: {X_train.shape}   y_train: {y_train.shape}")
print(f"  X_val  : {X_val.shape}   y_val  : {y_val.shape}")
print(f"  X_test : {X_test.shape}   y_test : {y_test.shape}")

N_FEATURES = X_train.shape[-1]

# tf.data pipelines
BATCH_SIZE = 64

train_ds = (
    tf.data.Dataset.from_tensor_slices((X_train, y_train))
    .shuffle(buffer_size=len(X_train), seed=42)
    .batch(BATCH_SIZE)
    .prefetch(tf.data.AUTOTUNE)
)
val_ds = (
    tf.data.Dataset.from_tensor_slices((X_val, y_val))
    .batch(BATCH_SIZE)
    .prefetch(tf.data.AUTOTUNE)
)

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 7 – Custom Layers (Kriteria 2)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[7/14] Mendefinisikan Custom Layers")
print("-" * 40)

# ── 7a. Custom Dense Layer (Kriteria 2: wajib) ──────────────────────────────
class CustomDenseLayer(tf.keras.layers.Layer):
    """Implementasi ulang Dense Layer dari nol menggunakan bobot eksplisit."""

    def __init__(self, units, activation=None, use_bias=True, **kwargs):
        super().__init__(**kwargs)
        self.units      = units
        self.activation = tf.keras.activations.get(activation)
        self.use_bias   = use_bias

    def build(self, input_shape):
        fan_in = int(input_shape[-1])
        # Glorot uniform initialization
        limit = np.sqrt(6.0 / (fan_in + self.units))
        self.W = self.add_weight(
            name="kernel",
            shape=(fan_in, self.units),
            initializer=tf.keras.initializers.RandomUniform(-limit, limit),
            trainable=True,
        )
        if self.use_bias:
            self.b = self.add_weight(
                name="bias",
                shape=(self.units,),
                initializer="zeros",
                trainable=True,
            )
        super().build(input_shape)

    def call(self, inputs):
        out = tf.matmul(inputs, self.W)
        if self.use_bias:
            out = out + self.b
        if self.activation is not None:
            out = self.activation(out)
        return out

    def get_config(self):
        cfg = super().get_config()
        cfg.update({"units": self.units,
                    "activation": tf.keras.activations.serialize(self.activation),
                    "use_bias": self.use_bias})
        return cfg


# ── 7b. Custom Multi-Head Attention Layer (Kriteria 2 – Advanced) ─────────────
class CustomMultiHeadAttention(tf.keras.layers.Layer):
    """
    Implementasi ulang Multi-Head Attention dari nol.
    Mengikuti "Attention is All You Need" (Vaswani et al., 2017).
    """

    def __init__(self, num_heads, key_dim, dropout=0.0, **kwargs):
        super().__init__(**kwargs)
        self.num_heads = num_heads
        self.key_dim   = key_dim
        self.dropout_rate = dropout
        self.depth     = key_dim * num_heads

    def build(self, input_shape):
        d_model = int(input_shape[-1])
        # Projection matrices
        self.Wq = self.add_weight(name="Wq", shape=(d_model, self.depth), initializer="glorot_uniform", trainable=True)
        self.Wk = self.add_weight(name="Wk", shape=(d_model, self.depth), initializer="glorot_uniform", trainable=True)
        self.Wv = self.add_weight(name="Wv", shape=(d_model, self.depth), initializer="glorot_uniform", trainable=True)
        self.Wo = self.add_weight(name="Wo", shape=(self.depth, d_model),  initializer="glorot_uniform", trainable=True)
        super().build(input_shape)

    def _split_heads(self, x):
        """x: (batch, seq, depth) → (batch, heads, seq, key_dim)"""
        batch = tf.shape(x)[0]
        seq   = tf.shape(x)[1]
        x = tf.reshape(x, (batch, seq, self.num_heads, self.key_dim))
        return tf.transpose(x, perm=[0, 2, 1, 3])

    def _scaled_dot_product(self, q, k, v):
        matmul_qk = tf.matmul(q, k, transpose_b=True)
        dk = tf.cast(self.key_dim, tf.float32)
        scores = matmul_qk / tf.math.sqrt(dk)
        weights = tf.nn.softmax(scores, axis=-1)
        if self.dropout_rate > 0.0:
            weights = tf.nn.dropout(weights, rate=self.dropout_rate)
        return tf.matmul(weights, v)

    def call(self, inputs, training=False):
        q = tf.matmul(inputs, self.Wq)   # (batch, seq, depth)
        k = tf.matmul(inputs, self.Wk)
        v = tf.matmul(inputs, self.Wv)

        q = self._split_heads(q)   # (batch, heads, seq, key_dim)
        k = self._split_heads(k)
        v = self._split_heads(v)

        attn = self._scaled_dot_product(q, k, v)   # (batch, heads, seq, key_dim)

        # Concatenate heads
        batch = tf.shape(attn)[0]
        seq   = tf.shape(attn)[2]
        attn  = tf.transpose(attn, perm=[0, 2, 1, 3])
        attn  = tf.reshape(attn, (batch, seq, self.depth))

        out = tf.matmul(attn, self.Wo)    # (batch, seq, d_model)
        return out

    def get_config(self):
        cfg = super().get_config()
        cfg.update({"num_heads": self.num_heads, "key_dim": self.key_dim, "dropout": self.dropout_rate})
        return cfg


# ── 7c. Custom Dropout Layer (Kriteria 2 – Advanced, opsi tambahan) ──────────
class CustomDropout(tf.keras.layers.Layer):
    """Implementasi ulang Dropout dari nol."""

    def __init__(self, rate, **kwargs):
        super().__init__(**kwargs)
        self.rate = rate

    def call(self, inputs, training=False):
        if training and self.rate > 0.0:
            # Inverted dropout
            keep = tf.cast(
                tf.random.uniform(tf.shape(inputs)) >= self.rate,
                dtype=inputs.dtype
            )
            return inputs * keep / (1.0 - self.rate)
        return inputs

    def get_config(self):
        cfg = super().get_config()
        cfg.update({"rate": self.rate})
        return cfg


print("  ✓ CustomDenseLayer")
print("  ✓ CustomMultiHeadAttention")
print("  ✓ CustomDropout")

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 8 – Model Baseline LSTM (Kriteria 1 & 2)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[8/14] Membangun Model Baseline LSTM")
print("-" * 40)

def build_lstm_baseline(window_size, n_features, forecast_horizon,
                        lstm_units=128, num_heads=4, key_dim=16, dropout=0.2):
    inp = keras.Input(shape=(window_size, n_features), name="lstm_input")

    # Custom Multi-Head Attention
    x = CustomMultiHeadAttention(num_heads=num_heads, key_dim=key_dim,
                                 dropout=dropout, name="mha")(inp)

    # Layer normalization (bawan Keras, bukan custom)
    x = layers.LayerNormalization(name="ln_1")(x)

    # Residual + LSTM
    x = layers.LSTM(lstm_units, return_sequences=False, name="lstm_1")(x)

    # Custom Dropout
    x = CustomDropout(dropout, name="custom_dropout")(x)

    # Custom Dense (output layer)
    out = CustomDenseLayer(forecast_horizon, activation="linear", name="output")(x)

    model = keras.Model(inputs=inp, outputs=out, name="LSTM_Baseline")
    return model


model_lstm = build_lstm_baseline(
    window_size=WINDOW_SIZE,
    n_features=N_FEATURES,
    forecast_horizon=FORECAST_HORIZON,
)
model_lstm.summary()

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 9 – Model Seq2Seq LSTM dengan Teacher Forcing (Kriteria 2)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[9/14] Membangun Model Seq2Seq LSTM (Teacher Forcing)")
print("-" * 40)

class Seq2SeqTeacherForcing(keras.Model):
    """
    Encoder–Decoder LSTM dengan Teacher Forcing.

    Saat training: decoder menerima ground-truth t-1 sebagai input.
    Saat inference: decoder menerima prediksi sebelumnya (autoregressive).
    """

    def __init__(self, encoder_units=128, decoder_units=128,
                 forecast_horizon=24, n_features=1, dropout=0.2, **kwargs):
        super().__init__(**kwargs)
        self.forecast_horizon = forecast_horizon
        self.encoder_units    = encoder_units
        self.decoder_units    = decoder_units

        # ── Encoder ──────────────────────────────────────────────────────────
        self.encoder_mha = CustomMultiHeadAttention(
            num_heads=4, key_dim=16, dropout=dropout, name="enc_mha")
        self.encoder_ln  = layers.LayerNormalization(name="enc_ln")
        self.encoder_lstm = layers.LSTM(
            encoder_units, return_state=True, name="encoder_lstm")
        self.encoder_drop = CustomDropout(dropout, name="enc_drop")

        # ── Decoder ──────────────────────────────────────────────────────────
        self.decoder_lstm   = layers.LSTMCell(decoder_units, name="decoder_cell")
        self.decoder_drop   = CustomDropout(dropout, name="dec_drop")
        # Projection: decoder hidden state → scalar prediction
        self.output_proj    = CustomDenseLayer(1, activation="linear", name="dec_proj")

    def encode(self, enc_input, training=False):
        x = self.encoder_mha(enc_input, training=training)
        x = self.encoder_ln(x + enc_input)
        _, h, c = self.encoder_lstm(x)
        h = self.encoder_drop(h, training=training)
        return h, c

    def call(self, inputs, training=False):
        """inputs: (enc_input, dec_input)  – dec_input only used during training"""
        enc_input, dec_input = inputs

        h, c = self.encode(enc_input, training=training)

        outputs = []
        # dec_input shape: (batch, forecast_horizon)  – Close values at t
        # First decoder input: last known Close from encoder window
        x_t = enc_input[:, -1, TARGET_IDX : TARGET_IDX + 1]  # (batch, 1)

        for t in range(self.forecast_horizon):
            out, [h, c] = self.decoder_lstm(x_t, states=[h, c])
            out = self.decoder_drop(out, training=training)
            pred_t = self.output_proj(out)    # (batch, 1)
            outputs.append(pred_t)

            # Teacher Forcing during training
            if training:
                x_t = dec_input[:, t : t + 1]   # ground-truth
            else:
                x_t = pred_t                     # use own prediction

        return tf.concat(outputs, axis=1)         # (batch, forecast_horizon)

    def predict_autoregressive(self, enc_input):
        """Autoregressive inference (no teacher forcing)."""
        h, c = self.encode(enc_input, training=False)
        outputs = []
        x_t = enc_input[:, -1, TARGET_IDX : TARGET_IDX + 1]
        for _ in range(self.forecast_horizon):
            out, [h, c] = self.decoder_lstm(x_t, states=[h, c])
            pred_t = self.output_proj(out)
            outputs.append(pred_t)
            x_t = pred_t
        return tf.concat(outputs, axis=1)


model_seq2seq = Seq2SeqTeacherForcing(
    encoder_units=128,
    decoder_units=128,
    forecast_horizon=FORECAST_HORIZON,
    n_features=N_FEATURES,
    name="Seq2Seq_LSTM",
)
# Build by calling once to initialise weights
_ = model_seq2seq(
    (X_train[:2], y_train[:2]),
    training=False,
)
model_seq2seq.summary()

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 10 – Custom Loss: Weighted Horizon MAE (Kriteria 3 – Advanced)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[10/14] Custom Loss – Weighted Horizon MAE")
print("-" * 40)

class WeightedHorizonLoss(tf.keras.losses.Loss):
    """
    MAE di mana setiap langkah horizon mendapat bobot yang meningkat.
    w_t = 1.0 + (t / horizon) * weight_factor

    Step jauh mendapat penalti lebih besar agar model bisa membuat
    prediksi yang lebih akurat pada horizon yang lebih panjang.
    """

    def __init__(self, forecast_horizon=24, weight_factor=1.0, **kwargs):
        super().__init__(**kwargs)
        self.forecast_horizon = forecast_horizon
        weights = np.array(
            [1.0 + (t / forecast_horizon) * weight_factor
             for t in range(forecast_horizon)],
            dtype=np.float32
        )
        # Normalise so sum = horizon (keeps scale comparable to plain MAE)
        self.weights = tf.constant(weights / weights.mean(), dtype=tf.float32)

    def call(self, y_true, y_pred):
        ae = tf.abs(y_true - y_pred)            # (batch, horizon)
        weighted = ae * self.weights             # broadcast over batch
        return tf.reduce_mean(weighted)

    def get_config(self):
        cfg = super().get_config()
        cfg.update({"forecast_horizon": self.forecast_horizon})
        return cfg


loss_fn = WeightedHorizonLoss(forecast_horizon=FORECAST_HORIZON, name="weighted_horizon_mae")

# Plain MAE metric untuk monitoring
def mae_metric(y_true, y_pred):
    return tf.reduce_mean(tf.abs(y_true - y_pred))

print("  ✓ WeightedHorizonLoss instantiated")
print(f"  Bobot per step: {loss_fn.weights.numpy()[:5]} ... (hanya 5 pertama)")

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 11 – Custom Callback: Reduce LR On Stagnation (Kriteria 3 – Advanced)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[11/14] Custom Callback – Reduce LR On Stagnation")
print("-" * 40)

class ReduceLROnStagnation(tf.keras.callbacks.Callback):
    """
    Mengurangi learning rate secara bertahap saat val_loss stagnan.

    Parameter
    ---------
    optimizer  : tf.keras.optimizers.Optimizer yang digunakan dalam custom loop
    patience   : jumlah epoch tanpa perbaikan sebelum LR dikurangi
    factor     : faktor pengurangan LR  (new_lr = lr * factor)
    min_lr     : batas bawah LR
    verbose    : cetak info saat LR dikurangi
    """

    def __init__(self, optimizer, patience=3, factor=0.5, min_lr=1e-6, verbose=True):
        super().__init__()
        self.optimizer  = optimizer
        self.patience   = patience
        self.factor     = factor
        self.min_lr     = min_lr
        self.verbose    = verbose
        self.wait       = 0
        self.best       = np.inf

    def on_epoch_end(self, epoch, logs=None):
        current = logs.get("val_loss", np.inf)
        if current < self.best - 1e-6:
            self.best = current
            self.wait = 0
        else:
            self.wait += 1
            if self.wait >= self.patience:
                old_lr = float(self.optimizer.learning_rate)
                new_lr = max(old_lr * self.factor, self.min_lr)
                self.optimizer.learning_rate.assign(new_lr)
                self.wait = 0
                if self.verbose:
                    print(f"\n  [ReduceLR] Epoch {epoch+1}: val_loss stagnan. "
                          f"LR {old_lr:.2e} → {new_lr:.2e}")


print("  ✓ ReduceLROnStagnation defined")

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 12 – Custom Training Loop dengan tf.GradientTape (Kriteria 3)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[12/14] Custom Training Loop (tf.GradientTape)")
print("-" * 40)

EPOCHS_LSTM    = 30
EPOCHS_SEQ2SEQ = 30
LR_INIT        = 1e-3

# ── Fungsi helper ─────────────────────────────────────────────────────────────

@tf.function
def train_step_lstm(model, X_batch, y_batch, optimizer, loss_fn):
    with tf.GradientTape() as tape:
        y_pred = model(X_batch, training=True)
        loss   = loss_fn(y_batch, y_pred)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    return loss, mae_metric(y_batch, y_pred)


@tf.function
def val_step_lstm(model, X_batch, y_batch, loss_fn):
    y_pred = model(X_batch, training=False)
    return loss_fn(y_batch, y_pred), mae_metric(y_batch, y_pred)


@tf.function
def train_step_seq2seq(model, X_batch, y_batch, optimizer, loss_fn):
    with tf.GradientTape() as tape:
        y_pred = model((X_batch, y_batch), training=True)
        loss   = loss_fn(y_batch, y_pred)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    return loss, mae_metric(y_batch, y_pred)


@tf.function
def val_step_seq2seq(model, X_batch, y_batch, loss_fn):
    y_pred = model((X_batch, y_batch), training=False)
    return loss_fn(y_batch, y_pred), mae_metric(y_batch, y_pred)


def run_training(model, train_ds, val_ds_data, epochs, loss_fn,
                 train_step_fn, val_step_fn, model_name):
    """Custom training loop universal untuk LSTM & Seq2Seq."""
    lr_var    = LR_INIT
    optimizer = tf.keras.optimizers.Adam(learning_rate=lr_var)
    reduce_lr = ReduceLROnStagnation(optimizer, patience=4, factor=0.5, min_lr=1e-6)

    history = {"loss": [], "mae": [], "val_loss": [], "val_mae": []}

    print(f"\n  Melatih {model_name} ({epochs} epoch) ...")
    print(f"  {'Epoch':>6}  {'Loss':>10}  {'MAE':>10}  {'Val Loss':>10}  {'Val MAE':>10}")
    print("  " + "-" * 55)

    X_val_arr, y_val_arr = val_ds_data

    for epoch in range(epochs):
        # ── Training ─────────────────────────────────────────────────
        epoch_loss, epoch_mae, n_batch = 0.0, 0.0, 0
        for X_batch, y_batch in train_ds:
            loss, mae = train_step_fn(model, X_batch, y_batch, optimizer, loss_fn)
            epoch_loss += loss.numpy()
            epoch_mae  += mae.numpy()
            n_batch    += 1

        epoch_loss /= n_batch
        epoch_mae  /= n_batch

        # ── Validation ───────────────────────────────────────────────
        val_loss_v, val_mae_v = val_step_fn(
            model, X_val_arr, y_val_arr, loss_fn
        )
        val_loss_v = val_loss_v.numpy()
        val_mae_v  = val_mae_v.numpy()

        history["loss"].append(epoch_loss)
        history["mae"].append(epoch_mae)
        history["val_loss"].append(val_loss_v)
        history["val_mae"].append(val_mae_v)

        # Callback
        reduce_lr.on_epoch_end(epoch, logs={"val_loss": val_loss_v})

        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f"  {epoch+1:>6}  {epoch_loss:>10.4f}  {epoch_mae:>10.4f}"
                  f"  {val_loss_v:>10.4f}  {val_mae_v:>10.4f}")

    print(f"  Training {model_name} selesai.\n")
    return history, optimizer


# Siapkan val batch (seluruh val set sekaligus untuk validasi)
X_val_full = tf.constant(X_val, dtype=tf.float32)
y_val_full = tf.constant(y_val, dtype=tf.float32)
X_test_tf  = tf.constant(X_test, dtype=tf.float32)
y_test_tf  = tf.constant(y_test, dtype=tf.float32)

# ── Latih LSTM Baseline ───────────────────────────────────────────────────────
history_lstm, _ = run_training(
    model     = model_lstm,
    train_ds  = train_ds,
    val_ds_data = (X_val_full, y_val_full),
    epochs    = EPOCHS_LSTM,
    loss_fn   = loss_fn,
    train_step_fn = train_step_lstm,
    val_step_fn   = val_step_lstm,
    model_name    = "LSTM Baseline",
)

# ── Latih Seq2Seq LSTM ────────────────────────────────────────────────────────
history_seq2seq, _ = run_training(
    model     = model_seq2seq,
    train_ds  = train_ds,
    val_ds_data = (X_val_full, y_val_full),
    epochs    = EPOCHS_SEQ2SEQ,
    loss_fn   = loss_fn,
    train_step_fn = train_step_seq2seq,
    val_step_fn   = val_step_seq2seq,
    model_name    = "Seq2Seq LSTM",
)

# ── Plot Training Curves ──────────────────────────────────────────────────────
def plot_training_history(history, title, save_path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    epochs_range = range(1, len(history["loss"]) + 1)

    ax1.plot(epochs_range, history["loss"],     label="Train Loss", color="#1f77b4")
    ax1.plot(epochs_range, history["val_loss"], label="Val Loss",   color="#ff7f0e", linestyle="--")
    ax1.set(title="Loss per Epoch", xlabel="Epoch", ylabel="Weighted MAE Loss")
    ax1.legend(); ax1.grid(True, alpha=0.3)

    ax2.plot(epochs_range, history["mae"],     label="Train MAE", color="#2ca02c")
    ax2.plot(epochs_range, history["val_mae"], label="Val MAE",   color="#d62728", linestyle="--")
    ax2.set(title="MAE per Epoch", xlabel="Epoch", ylabel="MAE")
    ax2.legend(); ax2.grid(True, alpha=0.3)

    fig.suptitle(title, fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(save_path, dpi=120)
    plt.close()
    print(f"  → Disimpan: {save_path}")


plot_training_history(
    history_lstm,
    "Training History – LSTM Baseline",
    os.path.join(OUTPUT_DIR, "training_lstm.png"),
)
plot_training_history(
    history_seq2seq,
    "Training History – Seq2Seq LSTM",
    os.path.join(OUTPUT_DIR, "training_seq2seq.png"),
)

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 13 – Inference & Evaluasi (Kriteria 3)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[13/14] Inference & Evaluasi pada Data Test")
print("-" * 40)

# ── Inverse scaling helper ────────────────────────────────────────────────────
def inverse_close(scaled_preds):
    """
    Kembalikan nilai Close dari skala normalised.
    Buat dummy array dengan semua kolom 0 kecuali TARGET_IDX,
    lalu inverse_transform dan ambil kolom TARGET_IDX.
    """
    n_samples  = scaled_preds.shape[0]
    n_steps    = scaled_preds.shape[1]
    n_feat     = len(FEATURES_EXT)

    out = np.zeros((n_samples * n_steps, n_feat))
    out[:, TARGET_IDX] = scaled_preds.reshape(-1)
    inv = scaler.inverse_transform(out)
    return inv[:, TARGET_IDX].reshape(n_samples, n_steps)


# ── LSTM Baseline Inference (direct multi-step) ───────────────────────────────
print("  LSTM Baseline – direct multi-step inference...")
y_pred_lstm_scaled = model_lstm(X_test_tf, training=False).numpy()   # (samples, 24)
y_pred_lstm_inv    = inverse_close(y_pred_lstm_scaled)
y_test_inv         = inverse_close(y_test)

mae_lstm_scaled = mean_absolute_error(y_test.reshape(-1), y_pred_lstm_scaled.reshape(-1))
mae_lstm_inv    = mean_absolute_error(y_test_inv.reshape(-1), y_pred_lstm_inv.reshape(-1))

print(f"  MAE LSTM Baseline (scaled) : {mae_lstm_scaled:.6f}")
print(f"  MAE LSTM Baseline (USD)    : {mae_lstm_inv:.2f}")

# ── Seq2Seq LSTM Inference (autoregressive) ───────────────────────────────────
print("  Seq2Seq LSTM – autoregressive inference...")
y_pred_seq2seq_scaled = model_seq2seq.predict_autoregressive(X_test_tf).numpy()
y_pred_seq2seq_inv    = inverse_close(y_pred_seq2seq_scaled)

mae_seq2seq_scaled = mean_absolute_error(y_test.reshape(-1), y_pred_seq2seq_scaled.reshape(-1))
mae_seq2seq_inv    = mean_absolute_error(y_test_inv.reshape(-1), y_pred_seq2seq_inv.reshape(-1))

print(f"  MAE Seq2Seq LSTM (scaled)  : {mae_seq2seq_scaled:.6f}")
print(f"  MAE Seq2Seq LSTM (USD)     : {mae_seq2seq_inv:.2f}")

# Cek apakah memenuhi kriteria < 0.015 (sebelum inverse scale)
flag = "✓ LULUS" if mae_seq2seq_scaled < 0.015 else "✗ Belum < 0.015"
print(f"\n  Kriteria Advanced MAE < 0.015 (scaled): {flag}  ({mae_seq2seq_scaled:.6f})")

# ── Visualisasi Line Chart Prediksi vs Aktual ─────────────────────────────────
print("\n  Membuat visualisasi prediksi...")

def plot_predictions(y_actual, y_pred_lstm, y_pred_seq2seq,
                     n_sequences=3, save_path=None):
    """
    Plot n_sequences contoh prediksi 24-step dari kedua model vs aktual.
    """
    indices = np.linspace(0, len(y_actual) - 1, n_sequences, dtype=int)
    fig, axes = plt.subplots(n_sequences, 1, figsize=(14, 5 * n_sequences))
    if n_sequences == 1:
        axes = [axes]

    for i, idx in enumerate(indices):
        steps = np.arange(1, FORECAST_HORIZON + 1)
        axes[i].plot(steps, y_actual[idx],       label="Aktual",        color="black",   linewidth=2)
        axes[i].plot(steps, y_pred_lstm[idx],    label="LSTM Baseline", color="#1f77b4", linestyle="--", linewidth=1.5)
        axes[i].plot(steps, y_pred_seq2seq[idx], label="Seq2Seq LSTM",  color="#d62728", linestyle="-.", linewidth=1.5)
        axes[i].set(title=f"Prediksi 24-Step (Sampel #{idx})",
                    xlabel="Horizon Step", ylabel="Harga Close (USD)")
        axes[i].legend(fontsize=10)
        axes[i].grid(True, alpha=0.3)
        axes[i].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

    fig.suptitle("Prediksi Harga Bitcoin (Test Set) – Multi-Step Forecasting",
                 fontsize=15, fontweight="bold", y=1.01)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=120, bbox_inches="tight")
        plt.close()
        print(f"  → Disimpan: {save_path}")
    else:
        plt.show()


plot_predictions(
    y_actual       = y_test_inv,
    y_pred_lstm    = y_pred_lstm_inv,
    y_pred_seq2seq = y_pred_seq2seq_inv,
    n_sequences    = 3,
    save_path      = os.path.join(OUTPUT_DIR, "prediksi_test.png"),
)

# ── Tabel Perbandingan Aktual vs Prediksi ─────────────────────────────────────
# Ambil satu contoh sequence untuk ditampilkan sebagai tabel
sample_idx = 0
steps      = np.arange(1, FORECAST_HORIZON + 1)

df_table = pd.DataFrame({
    "Step"             : steps,
    "Aktual (USD)"     : np.round(y_test_inv[sample_idx], 2),
    "LSTM Pred (USD)"  : np.round(y_pred_lstm_inv[sample_idx], 2),
    "Seq2Seq Pred (USD)": np.round(y_pred_seq2seq_inv[sample_idx], 2),
    "Selisih LSTM"     : np.round(np.abs(y_test_inv[sample_idx] - y_pred_lstm_inv[sample_idx]), 2),
    "Selisih Seq2Seq"  : np.round(np.abs(y_test_inv[sample_idx] - y_pred_seq2seq_inv[sample_idx]), 2),
})

print("\n  Tabel Perbandingan Aktual vs Prediksi (Sampel Pertama Test Set):")
print(df_table.to_string(index=False))

# Simpan tabel ke CSV
table_path = os.path.join(OUTPUT_DIR, "tabel_prediksi.csv")
df_table.to_csv(table_path, index=False)
print(f"\n  → Tabel disimpan: {table_path}")

# ── Ringkasan Evaluasi ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  RINGKASAN EVALUASI – TEST SET")
print("=" * 60)
print(f"  LSTM Baseline:")
print(f"    MAE (scaled) : {mae_lstm_scaled:.6f}")
print(f"    MAE (USD)    : ${mae_lstm_inv:.2f}")
print(f"  Seq2Seq LSTM:")
print(f"    MAE (scaled) : {mae_seq2seq_scaled:.6f}")
print(f"    MAE (USD)    : ${mae_seq2seq_inv:.2f}")
print(f"  Kriteria Advanced (<0.015 scaled): {flag}")
print("=" * 60)

# ─────────────────────────────────────────────────────────────────────────────
# BAGIAN 14 – Simpan Model (Kriteria File)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[14/14] Menyimpan Model")
print("-" * 40)

lstm_path    = os.path.join(OUTPUT_DIR, "model_baseline_LSTM.keras")
seq2seq_path = os.path.join(OUTPUT_DIR, "model_seq2seq_LSTM.keras")

model_lstm.save(lstm_path)
print(f"  ✓ LSTM Baseline disimpan    : {lstm_path}")

model_seq2seq.save(seq2seq_path)
print(f"  ✓ Seq2Seq LSTM disimpan     : {seq2seq_path}")

print("\n" + "=" * 60)
print("  SELESAI – Semua output berhasil dibuat!")
print("=" * 60)
print(f"  File yang dihasilkan:")
print(f"    • heatmap_korelasi.png")
print(f"    • acf_pacf.png")
print(f"    • training_lstm.png")
print(f"    • training_seq2seq.png")
print(f"    • prediksi_test.png")
print(f"    • tabel_prediksi.csv")
print(f"    • model_baseline_LSTM.keras")
print(f"    • model_seq2seq_LSTM.keras")
print("=" * 60)
