# Lapak Warga — Django Starter

Starter marketplace C2C dengan register, login, dashboard user, kategori, produk, keranjang, dan pesanan.

## 1. Persiapan
Pastikan Python sudah terpasang. Buka terminal pada folder project:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Secara default project menggunakan SQLite agar bisa langsung dicoba.

## 2. Jalankan project
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Buka http://127.0.0.1:8000/

## 3. Menggunakan MySQL
Buat database terlebih dahulu:
```sql
CREATE DATABASE lapak_warga CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
Atur variabel environment (atau salin `.env.example` menjadi `.env`; file `.env` belum otomatis dibaca pada starter ini):
```powershell
$env:DB_ENGINE="mysql"
$env:DB_NAME="lapak_warga"
$env:DB_USER="root"
$env:DB_PASSWORD="password_mysql_anda"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
```
Pastikan `mysqlclient` berhasil terpasang, lalu jalankan `python manage.py migrate`.

## 4. URL penting
- `/` — Beranda
- `/accounts/register/` — Registrasi
- `/accounts/login/` — Login
- `/accounts/logout/` — Logout
- `/dashboard/` — Dashboard user (wajib login)
- `/admin/` — Admin Django

## Catatan
- Autentikasi menggunakan sistem User bawaan Django dan password disimpan dengan hashing Django.
- Produk, kategori, keranjang, item keranjang, pesanan, dan item pesanan sudah disediakan sebagai model.
- Ini starter project untuk dikembangkan. Pembayaran online, verifikasi penjual, unggah gambar produk, dan checkout produksi belum diaktifkan.
