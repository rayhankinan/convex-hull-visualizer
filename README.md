# convex-hull-visualizer
Disusun untuk memenuhi Tugas Kecil 2 IF2211 Strategi Algoritma "Implementasi *Convex Hull* untuk Visualisasi Tes *Linear Separability* Dataset dengan Algoritma *Divide and Conquer*"

## Daftar Isi
* [Deskripsi Singkat Program](#deskripsi-singkat-program)
* [Struktur Program](#struktur-program)
* [Requirement Program](#requirement-program)
* [Cara Kompilasi Program](#cara-kompilasi-program)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Author](#author)

## Deskripsi Singkat Program
Permasalahan yang diangkat pada tugas kecil ini adalah memvisualisasikan data yang terdapat pada suatu dataset *classification* dan menganalisis apakah dataset tersebut dapat dipisahkan secara linear (*linearly separable*) atau tidak dengan menggunakan *convex hull*. Dataset yang dapat dianalisis menggunakan metode ini hanyalah dataset yang terdiri atas data-data numerik. Hal tersebut dikarenakan dibutuhkan teknik-teknik pengolahan data lanjut untuk menganalisis dataset yang mempunyari atribut kategorikal.<br>
*Convex hull* merupakan himpunan titik pada suatu bidang planar (*convex*) yang dimana jika sembarang dua titik pada himpunan tersebut dihubungkan oleh suatu garis, maka seluruh segmen garis tersebut terdapat di dalam himpunan tersebut. Dengan kata lain jika terdapat himpunan titik pada suatu bidang planar, maka *convex hull* merupakan poligon planar terkecil yang mencakup seluruh himpunan titik tersebut. Terdapat banyak aplikasi *convex hull*, seperti dalam kasus ini menjadi suatu pengujian apakah suatu dataset dapat dipisahkan secara linear atau tidak. Jika suatu dataset dapat dipisahkan secara linear, maka pemrogram dapat menggunakan model *machine learning* dengan tipe *linear classification* untuk memodelkan data tersebut. Untuk menentukan apakah suatu dataset *linearly separable* menggunakan visualisasi *convex hull* adalah dengan melakukan visualisasi untuk setiap pasangan atribut pada dataset tersebut. Ketika *convex hull* yang terbentuk untuk kategori atribut target yang berbeda terjadi *overlap* antara satu sama lain, maka dataset tersebut tidak bisa dipisahkan secara linear. Dataset dikatakan *linearly separable* ketika semua *convex hull* yang terbentuk dari hasil kombinasi dua atribut datasetnya tidak terdapat *overlap* sama sekali.<br>
Terdapat beberapa algoritma yang dapat digunakan untuk mencari *convex hull*, diantaranya adalah *Jarvis’s Algorithm* (menggunakan strategi *brute force*), *Graham Scan* (menggunakan strategi *sort and select*), serta *quickhull* (menggunakan strategi *divide and conquer*). Pada tugas kecil ini, penulis mengambil algoritma *quickhull* dikarenakan tingkat kompleksitasnya yang tidak terlalu rumit serta berkorelasi dengan materi kelas.<br>

### Visualisasi Algoritma Quickhull:
![Quickhull Algorithm](https://upload.wikimedia.org/wikipedia/commons/4/42/Animation_depicting_the_quickhull_algorithm.gif)

## Struktur Program
```bash
.
│   .gitignore
│   README.md
│   requirements.txt
│                   
├───src
│   │   myConvexHull.py
│   └───visualize.py
│           
└───test
        banknote.csv
        brain.csv
        heart.csv
        indiansdiabetes.csv
        list.txt
```

## Requirement Program
* Python versi 3.8.5 atau lebih baru. Pastikan pula terdapat package PyPi (PIP) pada Python Anda.

## Cara Kompilasi Program
1. Pastikan Python versi 3.8.5 atau lebih baru sudah terpasang pada mesin eksekusi (Anda dapat mengecek versi Python dengan menjalankan *command* `py --version` pada *command prompt*).
2. Lakukan instalasi semua *library* yang digunakan pada program. Anda dapat menginstalasi seluruh *library* yang digunakan pada program ini dengan menjalankan *command* `py -m pip install -r requirements.txt` pada *command prompt*.
3. Jika seluruh *library* berhasil diinstalasi, maka akan terdapat pemberitahuan pada *command prompt*.

## Cara Menjalankan Program
1. Bukalah *command prompt* pada *directory* program ini.
2. Jalankan *command* `py visualize.py <directory_dataset> <first_attribute> <second_attribute> -t <target_attribute> -c <list_of_class_name>` atau `py visualize.py <directory_dataset> <first_attribute> <second_attribute> --target <target_attribute> --class-name <list_of_class_name>` pada *command prompt*.
* **directory_dataset** berisi *relative path* dari *dataset* yang ingin dievaluasi.
* **first_attribute** berisi nama atribut pertama pada *dataset* yang ingin dievaluasi (atribut akan dijadikan sumbu X pada grafik).
* **second_attribute** berisi nama atribut kedua pada *dataset* yang ingin dievaluasi (atribut akan dijadikan sumbu Y pada grafik).
* **target_attribute** berisi nama atribut target pada *dataset* yang ingin dievaluasi (atribut akan dijadikan warna pada grafik).
* **list_of_class_name** berisi kumpulan *string* yang dipisahkan sebagai spasi yang menyatakan setiap nama kelas pada atribut target.
3. Catatan:
* Jika Anda masih bingung dengan penjelasan pada [README](https://github.com/rayhankinan/convex-hull-visualizer/blob/main/README.md), Anda dapat menjalankan *command* `py visualize.py -h` atau `py visualize.py --help` pada *command prompt* untuk melihat penjelasan mendetail tentang program.
* Jika Anda ingin menggunakan *dataset classification* bawaan *library* [scikit-learn](https://scikit-learn.org/), Anda dapat menghilangkan argumen **target_attribute** dan **class_name**.

## Author
* Nama: Rayhan Kinan Muhannad
* NIM: 13520065
* Prodi/Jurusan: STEI/Teknik Informatika
* Profile GitHub: [rayhankinan](https://github.com/rayhankinan)