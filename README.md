# Pertemuan 07 Fungsi Python

Nama: Keyla Maharani  
NIM: 2225250083  
Kelas: 3E

## 1. Tujuan

Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular. Praktik ini juga bertujuan memahami penggunaan perulangan, akumulator, nilai kembali, serta validasi input dalam program Python.

## 2. Cara Menjalankan

Program dijalankan melalui terminal VS Code dari folder utama proyek.

Latihan 1:
```bash
python3 latihan/01_fungsi_salam.py
```

Latihan 2:
```bash
python3 latihan/02_luas_persegi_panjang.py
```

Latihan 3:
```bash
python3 latihan/03_jumlah_n.py
```

Latihan 4:
```bash
python3 latihan/04_statistik_sederhana.py
```

Latihan 5:
```bash
python3 latihan/05_eksperimen_scope.py
```

Praktik 2:
```bash
python3 praktik/utilitas_matematika.py
```

Jika perintah `python3` tidak berfungsi di Windows, gunakan `python` sebagai penggantinya.

## 3. Struktur Fungsi

### A. Latihan 1 — Fungsi Salam

Nama fungsi: `salam(nama, kelas)`

Parameter:
- `nama`: nama orang yang akan disapa.
- `kelas`: kelas orang tersebut.

Fungsi menampilkan salam dan informasi kelas menggunakan `print()`.

### B. Latihan 2 — Luas Persegi Panjang

Nama fungsi: `luas_persegi_panjang(p, l)`

Parameter:
- `p`: panjang persegi panjang.
- `l`: lebar persegi panjang.

Return value: hasil perkalian panjang dan lebar, yaitu `p * l`.

### C. Latihan 3 — Jumlah 1 sampai n

Nama fungsi: `jumlah_n(n)`

Parameter:
- `n`: batas bilangan yang akan dijumlahkan.

Return value: jumlah bilangan dari 1 sampai n. Fungsi menggunakan perulangan `for` dan variabel `total` sebagai akumulator.

### D. Latihan 4 — Statistik Sederhana

Nama fungsi: `statistik(data)`

Parameter:
- `data`: kumpulan nilai dalam bentuk list.

Return value: tiga nilai, yaitu nilai minimum, nilai maksimum, dan rata-rata. Fungsi menggunakan perulangan untuk menghitung total dan mencari nilai minimum serta maksimum.

### E. Latihan 5 — Eksperimen Scope

Nama fungsi: `demo(x)`

Parameter:
- `x`: nilai yang diterima fungsi.

Return value: nilai `y`, yaitu `x + 5`.

Latihan ini menunjukkan perbedaan variabel lokal dan global. Parameter `x` di dalam fungsi tidak mengubah variabel global `x`.

### F. Praktik 2 — Utilitas Matematika Modular

1. `luas_persegi_panjang(p, l)`  
   Menghitung luas persegi panjang dan mengembalikan hasil perkalian panjang dan lebar.

2. `luas_segitiga(a, t)`  
   Menghitung luas segitiga dengan rumus setengah dikali alas dikali tinggi dan mengembalikan hasilnya.

3. `jumlah_n(n)`  
   Menghitung jumlah bilangan dari 1 sampai n menggunakan perulangan. Fungsi memvalidasi agar n merupakan bilangan bulat nonnegatif.

4. `faktorial(n)`  
   Menghitung faktorial menggunakan perulangan dan mengembalikan hasilnya. Nilai n harus berupa bilangan bulat nonnegatif. Faktorial 0 bernilai 1.

5. `tampilkan_menu()`  
   Menampilkan pilihan menu program dan tidak mengembalikan nilai perhitungan.

## 4. Hasil Pengujian

### A. Latihan 1 — Fungsi Salam

| Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| Nama = Keyla Maharani, Kelas = 3E | Menampilkan salam dan kelas | Halo, Keyla Maharani. Selamat belajar Python! Kelas: 3E | Berhasil |

### B. Latihan 2 — Luas Persegi Panjang

| Panjang | Lebar | Hasil yang Diharapkan | Hasil Aktual | Status |
|---:|---:|---:|---:|---|
| 8 | 5 | 40 | 40 | Berhasil |
| 2.5 | 4 | 10 | 10.0 | Berhasil |
| 0 | 7 | 0 | 0 | Berhasil |

### C. Latihan 3 — Jumlah 1 sampai n

| Nilai n | Hasil Perulangan | Hasil Rumus | Status |
|---:|---:|---:|---|
| 1 | 1 | 1 | Berhasil |
| 5 | 15 | 15 | Berhasil |
| 10 | 55 | 55 | Berhasil |
| 100 | 5050 | 5050 | Berhasil |

### D. Latihan 4 — Statistik Sederhana

Data yang digunakan: `[70, 80, 65, 90, 75]`.

| Pengujian | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---:|---:|---|
| Nilai minimum | 65 | 65 | Berhasil |
| Nilai maksimum | 90 | 90 | Berhasil |
| Nilai rata-rata | 76.0 | 76.0 | Berhasil |

### E. Latihan 5 — Eksperimen Scope

| Pengujian | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| Nilai di dalam fungsi | x = 20, y = 25 | x = 20, y = 25 | Berhasil |
| Nilai x di luar fungsi | 10 | 10 | Berhasil |
| Nilai hasil fungsi | 25 | 25 | Berhasil |

### F. Praktik 2 — Utilitas Matematika Modular

| No. | Pengujian | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Luas persegi panjang | p = 8, l = 5 | 40.0 | 40.0 | Berhasil |
| 2 | Luas segitiga | a = 10, t = 6 | 30.0 | 30.0 | Berhasil |
| 3 | Jumlah bilangan | n = 10 | 55 | 55 | Berhasil |
| 4 | Faktorial | n = 5 | 120 | 120 | Berhasil |
| 5 | Faktorial nol | n = 0 | 1 | 1 | Berhasil |
| 6 | Keluar dari program | Pilih menu 5 | Program berhenti | Program berhenti | Berhasil |

## 5. Refleksi

Bagian perhitungan luas persegi panjang menjadi lebih sederhana setelah dipisahkan ke dalam fungsi `luas_persegi_panjang(p, l)`. Perhitungan dapat dilakukan kembali dengan memanggil fungsi dan memberikan nilai panjang serta lebar sebagai argumen.

Fungsi `jumlah_n(n)` dan `faktorial(n)` juga membuat perhitungan lebih terstruktur karena masing-masing memiliki tugas yang jelas. Penggunaan `return` memungkinkan hasil fungsi disimpan dalam variabel atau digunakan dalam perhitungan lain.

Pada latihan scope, saya memahami bahwa parameter fungsi merupakan variabel lokal sehingga perubahan nilainya di dalam fungsi tidak otomatis mengubah variabel global. Modularisasi membuat program lebih mudah dibaca, diuji, dan diperbaiki.

## 6. Kesimpulan

Melalui Pertemuan 07, saya mempelajari cara membuat fungsi dengan `def`, menggunakan parameter dan argumen, mengembalikan hasil menggunakan `return`, serta memahami variabel lokal dan global.

Saya juga dapat menerapkan fungsi untuk menghitung luas, jumlah bilangan, statistik sederhana, dan faktorial. Dengan membagi program menjadi fungsi-fungsi kecil, kode menjadi lebih terstruktur, mudah digunakan kembali, dan lebih mudah diuji.
