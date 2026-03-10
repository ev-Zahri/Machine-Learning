# Weather Image Classification - Deep Learning Submission

Proyek ini adalah implementasi Convolutional Neural Network (CNN) untuk mengklasifikasikan kondisi cuaca berdasarkan gambar. Proyek ini bertujuan:
- Mengimplementasikan arsitektur Convolutional Neural Network (CNN) untuk pengenalan gambar secara otomatis.
- Mengklasifikasikan kondisi cuaca (Cloudy, Rainy, Shine, Sunrise) dengan tingkat akurasi minimal 85%.

## 1. Informasi Dataset
- **Sumber Dataset:** [Multi-class Weather Dataset (Kaggle)](https://www.kaggle.com/datasets/pratik2901/multiclass-weather-dataset)
- **Total Gambar:** 1,125 gambar.
- **Jumlah Kelas:** 4 Kelas (Cloudy, Rainy, Shine, Sunrise).
- **Pembagian Data:** 
    - **Train Set:** 80% (Data latih)
    - **Validation Set:** 10% (Evaluasi selama training)
    - **Test Set:** 10% (Evaluasi akhir/objektif)

## 2. Arsitektur Model
Model dibangun menggunakan Keras `Sequential` API dengan struktur sebagai berikut:
- **Convolutional Layers:** 4 lapis `Conv2D` untuk ekstraksi fitur gambar.
- **Pooling Layers:** `MaxPooling2D` untuk reduksi dimensi fitur.
- **Regularization:** `Dropout(0.5)` untuk mencegah overfitting.
- **Fully Connected Layer:** `Dense` layer dengan 512 neuron dan aktivasi `ReLU`.
- **Output Layer:** `Dense` layer dengan 4 neuron dan aktivasi `Softmax` untuk klasifikasi multi-kelas.

## 3. Hasil Performa
Model dilatih selama 50 epoch dengan fitur `EarlyStopping` dan `ReduceLROnPlateau` untuk stabilitas training.

| Metric | Hasil Akhir |
| :--- | :--- |
| **Training Accuracy** | ~94.22% |
| **Validation Accuracy** | ~90.99% |

## 4. Format Deployment
Model telah diekspor ke dalam tiga format utama untuk mendukung berbagai platform:
1. **SavedModel:** Format standar TensorFlow untuk deployment server.
2. **TF-Lite:** Format ringan untuk perangkat mobile dan IoT.
3. **TFJS:** Format JavaScript untuk dijalankan langsung di browser menggunakan `model.json`.

## 5. Cara Menjalankan Proyek
### Prasyarat
- Python 3.10 atau versi terbaru.
- Ruang penyimpanan sekitar 1-2 GB untuk library dan dataset.

### Langkah-Langkah:
1. **Clone/Download Proyek:**
   Download repository ini dan masuk ke direktori utama.

2. **Persiapkan Environment:**
   Sangat disarankan menggunakan virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   .\venv\Scripts\activate   # Untuk Windows
   ```
3. **Instalasi Library:**
   ```bash
   pip install -r requirements.txt
   ```
    Dependency yang diperlukan tercantum dalam file `requirements.txt`:
    - tensorflow
    - matplotlib
    - pandas
    - split-folders

4. **Persiapan Dataset:**
   ```bash
   - Ekstrak dataset ke folder bernama multi_class_weather_dataset.
   - Pastikan di dalamnya terdapat 4 folder kelas (Cloudy, Rainy, Shine, Sunrise).
   ```
5. **Jalankan Notebook:**
   ```bash
   - Buka file `notebook.ipynb`.
   - Jalankan sel-sel notebook secara berurutan.
   ```
6. (Optional) **Hasil model TFJS:**
   ```bash
   - Untuk menghasilkan model tensorflow.js perlu membuka colab lalu inputkan folder weather_model_saved yang sudah di zip. Lalu inputkan ke colab (di menu sisi kiri). Setelah itu jalankan tuliskan kode di notebook berikut:
   - !pip install tensorflowjs --quiet
   - !unzip sample_data/weather_model_saved.zip
   - input_dir = 'weather_model_saved'
     output_dir = 'tfjs_model'
     !tensorflowjs_converter \
        --input_format=tf_saved_model \
        {input_dir} \
        {output_dir}
   - !zip -r tfjs_model.zip tfjs_model
    
   ```
7. **Output:**
   ```bash
   - /weather_model_saved: Format SavedModel.
   - /tflite/weather_model.tflite: Format untuk tensorflow lite.
   - /tfjs_model/*: Folder berisi model untuk tensorflow.js.
   ```