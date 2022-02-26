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
        brain.csv
        heart.csv
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
* Jika Anda masih bingung dengan penjelasan pada README, Anda dapat menjalankan *command* `py visualize.py -h` atau `py visualize.py --help` pada *command prompt* untuk melihat penjelasan mendetail tentang program.
* Jika Anda ingin menggunakan *dataset classification* bawaan *library* scikit-learn, Anda dapat menghilangkan argumen target_attribute dan class_name.

## Author
* Nama: Rayhan Kinan Muhannad
* NIM: 13520065
* Prodi/Jurusan: STEI/Teknik Informatika
* Profile GitHub: [rayhankinan](https://github.com/rayhankinan)