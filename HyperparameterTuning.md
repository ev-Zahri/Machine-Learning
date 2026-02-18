Hyperparameter tuning merupakan langkah yang sangat penting untuk menghasilkan model machine learning yang andal. Tujuan utama hyperparameter tuning adalah untuk menemukan keseimbangan yang tepat antara bias dan varians (bias-variance tradeoff) sehingga model mampu mempelajari pola dengan baik tanpa kehilangan kemampuan untuk menggeneralisasi pada data baru.

Parameter vs Hyperparameter
![Parameter vs Hyperparameter](Parameter-vs-Hyperparameter.png)


cara untuk mengidentifikasi dan mengatur prioritas dalam tuning
1. Penggunaan Default Hyperparameter: Pada tahap awal dapat memberikan baseline yang cukup baik sebelum mulai melakukan tuning secara manual maupun otomatis.
2. Memahami Algoritma yang Digunakan:
    - Regresi Linier / Regresi Logistik: Regularisasi (L2 atau L1) dan C atau lambda adalah hyperparameter utama yang perlu diperhatikan.
    - K-Nearest Neighbors (KNN): Jumlah tetangga terdekat (k) dan jarak metrik (Euclidean, Manhattan) adalah hyperparameter yang paling penting.
    - Decision Tree: Kedalaman pohon (max_depth), jumlah sampel minimum untuk membagi simpul (min_samples_split), dan criterion (impurity measure seperti Gini atau Entropy) sangat memengaruhi performa model.
    - Random Forest: Jumlah pohon (n_estimators), kedalaman pohon (max_depth), dan ukuran minimum sampel di setiap daun (min_samples_leaf) adalah hyperparameter yang perlu dipertimbangkan.
    - Support Vector Machine (SVM): Regularisasi parameter (C) dan jenis kernel (linear, rbf, polynomial), serta parameter kernel seperti gamma (untuk rbf kernel) sangat penting.
    - Neural Networks (Jaringan Saraf Tiruan): Jumlah lapisan tersembunyi (hidden layer), jumlah neuron (units) di setiap lapisan, learning rate, batch size, dan optimizer sangat memengaruhi kinerja model.
3. Identifikasi Hyperparameter yang Paling Berpengaruh: Tidak semua hyperparameter memiliki pengaruh besar terhadap performa model. Fokus pada hyperparameter yang paling penting akan menghemat waktu dan sumber daya selama proses tuning.
4. Prioritaskan Tuning Hyperparameter yang Krusial: Tidak mencoba menyetel semua hyperparameter sekaligus, tetapi memfokuskan eksplorasi pada hyperparameter yang berpotensi memberikan dampak paling besar terlebih dahulu.
5. Memahami Hubungan antara Hyperparameter