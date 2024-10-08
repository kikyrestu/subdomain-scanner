Berikut adalah **README.md** yang sesuai untuk proyek pemindaian subdomain dengan Python:

```md
# Pemindaian Subdomain dengan Python

Proyek ini adalah skrip Python yang dirancang untuk memindai subdomain dari sebuah domain menggunakan permintaan HTTP. Skrip ini membaca daftar subdomain dari file teks dan memeriksa mana yang aktif dengan menggunakan threading untuk meningkatkan kecepatan pemindaian.

## 📚 Deskripsi Proyek

Skrip ini melakukan pemindaian subdomain dengan cara:
1. Membaca subdomain dari file teks.
2. Menggunakan threading untuk memeriksa status setiap subdomain secara bersamaan.
3. Mencetak subdomain yang aktif berdasarkan respons HTTP dari server.

## 🛠️ Teknologi yang Digunakan

- **Python**: Bahasa pemrograman utama untuk skrip ini.
- **Requests**: Library untuk membuat permintaan HTTP.
- **ThreadPoolExecutor**: Dari `concurrent.futures`, digunakan untuk pemrograman multithreading.

## ⚙️ Cara Menjalankan Proyek

### Prasyarat

Pastikan Anda telah menginstal Python dan library `requests`. Jika belum, Anda dapat menginstalnya menggunakan pip:

```bash
pip install requests
```

### Langkah-langkah Menjalankan:

1. **Kloning Repository**:
   ```bash
   git clone https://github.com/kikyrestu/subdomain-scanner.git
   cd subdomain-scanner
   ```

2. **Siapkan Daftar Subdomain**:
   - Buat file teks bernama `subdomains-10000.txt` di direktori yang sama dengan skrip. Pastikan file ini berisi daftar subdomain yang ingin Anda periksa, satu subdomain per baris.

3. **Jalankan Skrip**:
   ```bash
   python subdomain_scanner.py
   ```
   - Masukkan domain Anda ketika diminta, misalnya `example.com`.

## 📋 Contoh Penggunaan

```
Masukkan domain Anda: example.com
Memindai subdomain untuk example.com...

Subdomain yang aktif ditemukan:
http://www.example.com
http://api.example.com
```

## 👨‍💻 Creator

- **Nama**: Kiky Restu Noviansyah
- **Email**: kikyrestunov@gmail.com
