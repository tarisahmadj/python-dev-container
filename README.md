# python-dev-container

Project ini adalah sebuah *Development Environment* (Lingkungan Pengembangan) berbasis Docker untuk Python. Ini dirancang khusus agar mudah digunakan oleh developer untuk menulis dan menjalankan kode Python secara interaktif, tanpa perlu menginstal Python langsung di komputer lokal.

## 🌟 Fitur Utama
- **Persistent Packages**: Menggunakan fitur *Bind Mount* ke folder lokal (`.pip_packages`). Semua *library* yang Anda instal melalui `pip` di dalam container akan tersimpan di laptop Anda. Anda tidak akan kehilangan library yang sudah diinstal meskipun container dimatikan atau dihancurkan.
- **Non-Root User**: Berjalan menggunakan user khusus `devuser` (UID 1000) untuk menghindari masalah permission (hak akses) pada file yang dibuat di dalam container (menjaga file tetap bisa diedit secara normal di macOS/Linux lokal).
- **Auto-Sync Code**: Folder `src` dihubungkan secara langsung ke dalam container (`/app`). Apapun kode `.py` yang Anda tulis/edit di VS Code lokal Anda akan langsung terbaca di dalam container.
- **Unbuffered Output**: Fitur `PYTHONUNBUFFERED=1` diaktifkan agar output terminal seperti `print()` muncul secara instan.

## 📂 Struktur Direktori

```text
.
├── .pip_packages/       # (Otomatis dibuat) Folder fisik tempat pip menyimpan library Anda
├── src/                 # Folder utama tempat Anda meletakkan kode program Python (.py)
│   ├── main.py          # Script utama untuk menjalankan semua modul testing
│   ├── module_a.py      # Modul test A
│   ├── module_b.py      # Modul test B
│   ├── module_numpy.py  # Contoh implementasi library Numpy
│   └── module_requests.py # Contoh implementasi library Requests
├── Dockerfile           # Konfigurasi spesifikasi container (Python 3.11-slim)
├── docker-compose.yml   # Konfigurasi service container dan volume bind-mount
└── requirements.txt     # Daftar dependensi library (numpy, requests, dll.)
```

## 🛠 Cara Penggunaan

### 1. Menjalankan Container
Buka terminal Anda (di komputer lokal, pada folder proyek ini), lalu jalankan:
```bash
docker-compose up -d --build
```
*Perintah ini akan membuat dan menjalankan container di latar belakang (background).*

### 2. Masuk ke dalam Container (Bash Shell)
Untuk menjalankan kode, Anda harus masuk ke dalam terminal containernya:
```bash
docker-compose exec app bash
```

### 3. Menginstal Dependensi (Library)
Di dalam terminal container, instal library yang dibutuhkan. Karena kita menggunakan fitur bind mount, Anda hanya perlu melakukan ini sekali saja:
```bash
pip install -r requirements.txt
# atau install satuan secara manual:
# pip install numpy requests
```

### 4. Menjalankan Program
Masih di dalam terminal container, jalankan kode utama:
```bash
python main.py
```
Program akan mengeksekusi semua modul yang ada dan mencetak output yang menunjukkan dari file mana fungsi tersebut dipanggil.

### 5. Mematikan Container
Jika Anda sudah selesai bekerja dan ingin mematikan container:
```bash
# Keluar dari container dulu:
exit 

# Matikan container dari terminal lokal:
docker-compose down
```
*Tenang saja, instalasi `pip` Anda tetap aman di folder `.pip_packages` meskipun Anda menjalankan `docker-compose down`.*
