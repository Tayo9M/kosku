# Instruksi Implementasi Chart.js untuk Statistik

Dokumen ini berisi petunjuk untuk mengimplementasikan visualisasi statistik menggunakan Chart.js di PythonAnywhere.

## Langkah-langkah Implementasi

### 1. Upload File Template

Upload file-file template berikut ke folder templates di PythonAnywhere:

- `room_stats_js.html`
- `financial_stats_js.html`

### 2. Update Fungsi di routes.py

Ganti fungsi `room_stats()` dan `financial_stats()` di file `routes.py` dengan fungsi yang ada di `routes_chartjs.py`.

Pastikan untuk menambahkan import json di bagian atas file routes.py jika belum ada:

```python
import json
```

### 3. Lokasi Penggantian Fungsi

Fungsi `room_stats()` dimulai pada baris sekitar 638 di `routes.py`.
Fungsi `financial_stats()` dimulai pada baris sekitar 733 di `routes.py`.

Ganti seluruh isi fungsi (dari `def room_stats():` sampai fungsi berikutnya, dan dari `def financial_stats():` sampai fungsi berikutnya).

### 4. Perbaikan Error Decimal di JSON

Pastikan kode untuk mengatasi error "Object of type Decimal is not JSON serializable" sudah diterapkan:

1. Semua nilai numerik yang dikonversi ke JSON (menggunakan `json.dumps()`) harus dikonversi ke tipe data `float` atau `int`.
2. Lihat fungsi di `routes_chartjs.py` untuk contoh konversi yang benar.

### 5. Reload Aplikasi

Setelah semua perubahan diterapkan, reload aplikasi web di PythonAnywhere.

## Troubleshooting

### Template Not Found

Jika muncul error "Template not found", pastikan:
- File template sudah diupload ke folder templates
- Nama file yang dirujuk di dalam fungsi sudah benar (case sensitive)

### Decimal JSON Error

Jika masih mendapatkan error "Object of type Decimal is not JSON serializable":
- Pastikan semua nilai dari database dikonversi ke tipe data float sebelum dijadikan JSON
- Periksa kode konversi di `routes_chartjs.py` untuk referensi

### Visualisasi Tidak Muncul

Jika grafik tidak muncul:
- Periksa Console di browser untuk melihat error JavaScript
- Pastikan Chart.js berhasil dimuat dari CDN
- Pastikan data yang dikirim untuk Chart.js valid (tidak null atau undefined)

## Catatan Penting

1. File `routes_chartjs.py` hanya berisi fungsi-fungsi yang perlu diganti, jangan ganti seluruh file `routes.py` dengan file ini.
2. Pastikan tidak ada import atau dependensi matplotlib di fungsi Chart.js yang baru.
3. Semua rendering grafik dilakukan oleh browser menggunakan JavaScript, bukan di server.

Jika mengalami kesulitan, bisa juga mencoba menggunakan versi template tanpa grafik (`room_stats_no_chart.html` dan `financial_stats_no_chart.html`) sebagai alternatif.