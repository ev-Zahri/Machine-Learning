Deep learning adalah bagian dari bidang kecerdasan buatan dengan menggunakan algoritma yang terinspirasi dari cara otak manusia bekerja. Metode ini diimplementasikan melalui jaringan saraf tiruan yang disebut artificial neural networks atau disingkat sebagai ANN. 

ANN adalah model matematis yang terdiri dari tiga atau lebih lapisan neuron yang saling terhubung.

Keunggulan utama deep learning terletak pada kemampuannya untuk belajar secara mandiri dari data yang besar dan kompleks. Proses pembelajaran ini melibatkan penyesuaian bobot dan parameter jaringan secara iteratif melalui proses yang disebut pelatihan (training), ketika model diuji dan diperbaiki berdasarkan umpan balik dari data.

Terms pada Neural Network
1. Activation Function (Fungsi Aktivasi) adalah sebuah fungsi matematika yang menentukan bahwa neuron dalam jaringan saraf tiruan akan menghasilkan output atau tidak berdasarkan inputnya.

Fungsi aktivasi pada perceptron bertugas untuk membuat jaringan saraf mampu menyesuaikan pola dengan data non linier. Ada beberapa jenis fungsi aktivasi yang umum digunakan dalam jaringan saraf sebagai berikut.
a. Linear activation function (fungsi aktivasi linear) adalah sebuah fungsi dengan keluaran yang proporsional secara linear terhadap input. Dengan kata lain, fungsi ini hanya melakukan transformasi linear sederhana dari input ke output tanpa memperkenalkan non-linearitas.

b. ReLU (rectified linear activation) adalah jenis fungsi aktivasi yang umum digunakan dalam jaringan saraf tiruan. Fungsi ReLU didefinisikan sebagai f(x) = max(0, x). Ini berarti output dari ReLU adalah nilai inputnya jika nilai input tersebut lebih besar dari atau sama dengan nol, dan output-nya adalah nol jika nilai inputnya kurang dari nol.

Keuntungan utama dari ReLU adalah sederhana pada komputasi dan memperkenalkan non-linearitas ke dalam jaringan. ReLU umumnya digunakan sebagai fungsi aktivasi pada lapisan tersembunyi karena kemampuannya untuk mempercepat konvergensi pembelajaran dan mengurangi risiko overfitting.
 
c. Leaky ReLU adalah beberapa gradien dapat menjadi sangat rapuh selama proses pelatihan, yang dapat menyebabkan fenomena "neuron mati". Ini berarti bahwa selama pelatihan, beberapa neuron dapat terkunci dalam keadaan mereka tidak akan pernah diaktifkan lagi pada sebagian besar atau semua data yang diberikan. Hal itu terjadi karena gradien (turunan) dari fungsi ReLU menjadi nol pada bagian negatifnya.

d. Sigmoid akan menerima angka tunggal dan mengubah x menjadi sebuah nilai yang memiliki rentang mulai dari 0 sampai 1. Fungsi ini biasanya dapat diinterpretasikan sebagai probabilitas dalam konteks klasifikasi biner.

Keuntungan utama dari sigmoid adalah kemampuannya dalam menghasilkan keluaran dengan batas antara 0 dan 1, yang berguna untuk tugas klasifikasi ketika kita ingin memprediksi probabilitas keanggotaan pada kelas tertentu.

e. Tanh (hyperbolic tangent) adalah jenis fungsi aktivasi lain yang umum digunakan dalam jaringan saraf tiruan. Tanh akan mengubah nilai input x-nya menjadi sebuah nilai yang memiliki rentang mulai dari -1 hingga 1.

tanh juga memiliki beberapa masalah, seperti rentang output yang terbatas (-1 sampai 1). Ini juga bisa menyebabkan gradien menghilang pada jaringan.

f. Softmax adalah jenis fungsi aktivasi yang umum digunakan pada lapisan output dari jaringan saraf, terutama untuk tugas klasifikasi multiclass. Fungsi softmax mengubah nilai input menjadi distribusi probabilitas yang memetakan output pada rentang (0, 1) sehingga total probabilitas output menjadi 1.

Arsitektur Deep Learning
1. Input layer adalah bagian pertama dari jaringan neural yang bertanggung jawab untuk menerima data masukan, yaitu gambar, teks, atau data numerik lainnya. Fungsi utama dari input layer adalah meneruskan data masukan ke lapisan-lapisan selanjutnya dalam jaringan, yang disebut sebagai hidden layers.

2. Hidden Layer adalah lapisan-lapisan di antara input layer dan output layer dalam jaringan neural. Tugas utama dari hidden layers adalah untuk mengekstrak fitur-fitur yang semakin abstrak dan kompleks dari data masukan yang telah diteruskan oleh input layer. 
Ada banyak jenis hidden layer seperti: fully connected layer, convolutional layer, batch normalization layer, recurrent layer, dropout layer, pooling layer, dan flatten layer.

3. Output layer adalah layer terakhir dalam deep learning yang menghasilkan output berdasarkan hasil pemrosesan oleh hidden layer. Jumlah neuron dalam output layer bergantung pada tipe tugas yang ingin diselesaikan oleh jaringan.


Arsitektur deep learning
1. Convolutional Neural Network (CNN) adalah jenis arsitektur deep learning yang dirancang khusus untuk memproses data gambar dan visual dengan efisien. CNN terdiri atas serangkaian lapisan yang dapat mengekstrak fitur-fitur hierarkis dari gambar secara bertahap.
Karakteristik: Convolutional layer, pooling layer, fully connected layer, dan activation layer.
Penggunaan Umum: Pengenalan gambar dan objek, klasifikasi citra, segmentasi gambar.

2. Recurrent neural network (RNN) adalah arsitektur deep learning yang dirancang untuk memproses data berurutan, seperti teks, audio, atau time series data. RNN memiliki kemampuan untuk "mengingat" informasi dari iterasi sebelumnya melalui loop rekursif.
Karakteristik: Recurrent loop, mempry cell
Penggunaan Umum: Pemrosesan bahasa alami, pengenalan suara dan pengolahan sinyal audio dan prediksi time series.

3. Long short-term memory (LSTM) adalah jenis RNN yang ditingkatkan dengan mekanisme gate untuk mengatasi masalah hilangnya informasi jangka panjang dalam pembelajaran berurutan.
Karakteristik: Forget gate, input gate.
Penggunaan Umum: Pemrosesan bahasa alami, pengenalan wicara dan pemrosesan sinyal audio.

4. Generative adversarial network (GAN) adalah arsitektur deep learning terdiri dari dua jaringan neural berlawanan yang saling bersaing, yaitu generator dan diskriminator.
Karakteristik: Generator dan Diskriminator
Penggunaan Umum: Menghasilkan gambar sintesis untuk aplikasi kreatif, pemberdayaan data dan augmentasi dataset

5. Transformer adalah arsitektur deep learning berbasis atensi (attention-based) yang digunakan, terutama dalam pemrosesan bahasa alami untuk mengatasi masalah ketergantungan jarak panjang.
karakteristik: Mekanisme self-attention, encoder block dan decoder block
Penggunaan Umum: Penerjemah mesin lintas bahasa, pemodelan bahasa untuk tugas NLP

6. Autoencoder adalah arsitektur deep learning yang digunakan untuk melakukan reduksi dimensi atau generasi data sintetis
Karakteristik: Encoder dan decoder
Penggunaan Umum: Reduksi dimensi, denoising data, dan generasi data sintetis
