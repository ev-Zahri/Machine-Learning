Teknik Mengatasi Overfitting dan Underfitting

- Overfitting terjadi ketika model terlalu kompleks dan terlalu "menghafal" data latih sehingga tidak dapat menggeneralisasi pada data baru.
- Underfitting terjadi ketika model terlalu sederhana sehingga tidak cukup menangkap pola-pola dalam data.

Teknik Mengatasi Overfitting
1. Cross-Validation: Teknik ini membagi data menjadi beberapa subset yang dikenal sebagai fold. Model dilatih dalam beberapa subset serta diuji pada subset yang tersisa dan proses ini diulang beberapa kali. Jika performa model sangat bervariasi antara fold, ini menunjukkan bahwa model mengalami overfitting pada subset data tertentu dan tidak dapat menggeneralisasi dengan baik. Cross-validation membantu memastikan bahwa model dinilai secara lebih konsisten di seluruh data.
2. Early Stopping: Cara kerjanya cukup sederhana, yaitu ketika kita melatih model, data dibagi menjadi dua bagian, yaitu data training (data latih) dan data validation (data validasi). Model dilatih menggunakan data latih, sementara kita memantau kinerjanya menggunakan data validasi. Early stopping menghentikan pelatihan yang saat ini terjadi sehingga model tidak berlatih terlalu lama dan bisa bekerja lebih baik saat dihadapkan pada data baru.
3. Regularization: Teknik yang digunakan dalam machine learning untuk mengurangi kompleksitas model dan mencegah overfitting dengan menambahkan penalti pada ukuran koefisien model. Tujuan utama dari regularisasi adalah menjaga model agar tetap sederhana dan menghindari penyesuaian yang berlebihan terhadap data pelatihan
- Jenis-Jenis Regularization
    - L1 Regularization (Lasso): cara untuk menyederhanakan model dengan mengurangi koefisien fitur yang kurang penting hingga menjadi nol. Ini artinya, fitur-fitur yang tidak relevan akan diabaikan oleh model.
    - L2 Regularization (Ridge): menambahkan penalti untuk koefisien fitur yang terlalu besar. Dalam arti lain, teknik ini membuat model lebih sederhana dengan mengurangi ukuran koefisien, tetapi tidak menghilangkan fitur sama sekali.
    - Elastic Net: kombinasi dari L1 dan L2 regularization. tidak hanya memilih fitur penting, seperti L1, tetapi juga mencegah fitur menjadi terlalu dominan, seperti L2.
4. Dropout: teknik penting untuk mencegah model neural network terlalu menyesuaikan diri dengan data latih, yang dikenal sebagai overfitting. Selama proses pelatihan, beberapa neuron dalam jaringan "dibuang" atau dinonaktifkan secara acak. Ini berarti neuron-neuron tidak berfungsi dalam perhitungan untuk sementara waktu. cara ini, model tidak bergantung pada neuron tertentu dan harus belajar untuk bekerja dengan berbagai neuron yang tersedia. Hasilnya, model menjadi lebih fleksibel dan mampu mengenali pola yang lebih umum, bukan hanya detail spesifik dari data latih. 
5. Data augmentation: teknik penting yang digunakan untuk meningkatkan jumlah dan variasi data pelatihan tanpa harus mengumpulkan data baru. Dengan membuat modifikasi atau variasi pada data yang sudah ada, teknik ini membantu model machine learning menjadi lebih tangguh dan mampu menangani berbagai situasi berbeda di dunia nyata. Keuntungan utama dari data augmentation adalah model menjadi lebih robust dan adaptif terhadap variasi data.
6. Pruning: teknik yang umumnya diterapkan pada pohon keputusan untuk menyederhanakan model dengan mengurangi kompleksitasnya. Tujuannya adalah meningkatkan kemampuan model dalam menggeneralisasi data baru dengan menghilangkan cabang-cabang pohon yang tidak memberikan kontribusi signifikan terhadap hasil akhir.
- Jenis-Jenis Pruning
    - Pre-Pruning: Dalam proses ini, kita menghentikan penambahan cabang baru ke pohon keputusan saat masa pelatihan.
    - Post-Pruning: Setelah pohon keputusan selesai dibentuk, kita melakukan pemangkasan untuk menghapus cabang-cabang yang tidak banyak membantu dalam membuat keputusan. Caranya adalah memeriksa seberapa baik setiap cabang berkontribusi pada akurasi model. Cabang yang memberikan kontribusi kecil akan dihapus untuk menyederhanakan model. 


Teknik Mengatasi Underfitting
1. Tambahkan Data Latih: Jika model Anda mengalami underfitting, artinya ia tidak dapat menangkap pola atau hubungan yang relevan dalam data dengan baik. Salah satu cara untuk memperbaiki masalah ini adalah memberikan model lebih banyak data untuk dipelajari. Penting untuk memastikan bahwa data yang Anda tambahkan relevan dan berkualitas tinggi. Data yang tidak relevan atau memiliki kualitas buruk dapat memperburuk masalah dan menyebabkan model belajar dari informasi tidak berguna
2. Tambahkan Lebih Banyak Fitur: Semakin relevan serta informatif fitur yang Anda sediakan, semakin baik model dalam memahami dan memprediksi hasil. Jika model Anda mengalami underfitting, bisa jadi fitur tidak cukup memberikan informasi yang diperlukan. Semakin relevan serta informatif fitur yang Anda sediakan, semakin baik model dalam memahami dan memprediksi hasil. Jika model Anda mengalami underfitting, bisa jadi fitur tidak cukup memberikan informasi yang diperlukan.
3. Eksperimen dengan Hyperparameter Tuning: Jika hyperparameter tidak diatur dengan baik, model bisa menjadi terlalu sederhana (underfitting) atau terlalu rumit (overfitting). Oleh karena itu, menyesuaikan hyperparameter dengan tepat bisa meningkatkan kinerja model secara signifikan.






