import pandas as pd

# Dokumen
d1 = "Python adalah bahasa pemrograman tingkat tinggi yang sangat ekspresif dan mudah dibaca. SQL adalah bahasa query yang digunakan untuk berinteraksi dengan database."


d2 = "Pada masa lalu, komputer digunakan terutama untuk pemrosesan data bisnis. ,Sekarang, komputer telah menjadi alat yang sangat penting dalam berbagai aspek kehidupan."


d3 = "Machine learning adalah cabang dari kecerdasan buatan yang fokus pada pengembangan algoritma. Dengan machine learning, komputer dapat belajar dari data dan membuat keputusan atau prediksi tanpa harus diprogram secara eksplisit. Ini memungkinkan komputer untuk melakukan tugas-tugas yang kompleks seperti pengenalan suara atau pengenalan wajah."

d4 = "Algoritma genetika adalah metode optimasi berbasis populasi yang terinspirasi oleh evolusi. Mereka digunakan untuk memecahkan masalah optimasi kompleks di berbagai bidang seperti ilmu komputer, ekonomi, dan biologi. Algoritma genetika bekerja dengan cara menggabungkan sifat-sifat dari solusi-solusi yang ada untuk menciptakan solusi baru."


d5 = "HTML adalah bahasa markup yang digunakan untuk membuat halaman web. HTML terdiri dari berbagai elemen yang mendefinisikan struktur dari sebuah halaman web. Setiap elemen memiliki peran dan atributnya sendiri untuk membentuk tata letak dan konten halaman web." 


d6 = "Pengolahan citra adalah cabang ilmu komputer yang berkaitan dengan analisis dan manipulasi gambar. Dalam pengolahan citra, kita dapat melakukan berbagai operasi seperti pemrosesan, analisis fitur, dan pengenalan pola. Aplikasi dari pengolahan citra mencakup pengenalan wajah, deteksi objek, dan restorasi citra."


d7 = "Ruang hampa adalah medium di mana tidak ada materi. Ini adalah konsep penting dalam fisika dan memainkan peran besar dalam teori relativitas dan kosmologi."


d8 = "Statistik adalah cabang ilmu matematika yang berkaitan dengan pengumpulan dan analisis data. Statistik digunakan dalam berbagai bidang untuk mendapatkan wawasan dan membuat keputusan berdasarkan data yang ada. Metode statistik termasuk penghitungan rata-rata, deviasi standar, dan analisis regresi."


d9 = "Pengkodean adalah proses mengubah informasi menjadi format yang dapat dipahami oleh komputer. Terdapat berbagai bahasa pemrograman yang digunakan untuk melakukan pengkodean, termasuk Python, Java, dan C++. Setiap bahasa memiliki sintaks dan aturan sendiri untuk memandu cara menulis kode."


d10 = "Keamanan cyber menjadi semakin penting di era digital ini. Perlindungan terhadap serangan siber dan kebocoran data adalah hal-hal yang sangat diperhatikan oleh organisasi dan individu. Dengan adanya teknologi baru, risiko keamanan juga semakin kompleks dan memerlukan solusi yang canggih."

documents = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]

dataset_pak_hendra = pd.DataFrame({'text': documents})
dataset_pak_hendra.head(10)
dataset_pak_hendra.to_csv('.dataset.csv', index=False)