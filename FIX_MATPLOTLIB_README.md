# Cara Mengatasi Masalah Matplotlib di PythonAnywhere

Panduan ini menjelaskan cara mengatasi masalah RecursionError pada Matplotlib di PythonAnywhere. PythonAnywhere memiliki beberapa keterbatasan yang dapat menyebabkan error pada fungsi-fungsi yang menggunakan Matplotlib untuk visualisasi data.

## Masalah yang Dihadapi

Error yang muncul ketika mengakses halaman statistik:

```
RecursionError: maximum recursion depth exceeded while calling a Python object
```

Error ini terjadi pada penggunaan Matplotlib di PythonAnywhere karena keterbatasan lingkungan hosting tersebut.

## Solusi

Aplikasi ini sudah dilengkapi dengan solusi alternatif menggunakan Chart.js untuk memvisualisasikan data tanpa perlu menggunakan Matplotlib. Chart.js adalah library JavaScript yang dapat menampilkan grafik interaktif di browser.

### Perubahan yang Dilakukan

1. File `routes_chartjs.py` berisi versi Chart.js dari fungsi-fungsi visualisasi yang ada di `routes.py`.
2. File `templates/room_stats_js.html` dan `templates/financial_stats_js.html` berisi template HTML dengan Chart.js.
3. File `fix_matplotlib_issues.py` adalah script otomatis untuk menerapkan solusi ini.

### Cara Menerapkan Solusi

Solusi Chart.js sudah otomatis diterapkan dalam aplikasi ini. File `main.py` sudah dimodifikasi untuk mengimpor Chart.js sebagai pengganti matplotlib.

Jika Anda mengalami masalah, Anda dapat menjalankan script berikut untuk menerapkan solusi secara manual:

```bash
python fix_matplotlib_issues.py
```

Kemudian restart aplikasi Anda.

## Keuntungan Menggunakan Chart.js

1. **Performa Lebih Baik**: Chart.js berjalan di sisi klien (browser), sehingga tidak membebani server.
2. **Interaktif**: Pengguna dapat berinteraksi dengan grafik (hover, klik, dll).
3. **Tampilan Lebih Menarik**: Chart.js menyediakan animasi dan tampilan yang lebih modern.
4. **Kompatibilitas**: Bekerja di semua browser modern dan perangkat mobile.

## Konfigurasi Tambahan

Tidak diperlukan konfigurasi tambahan, semua sudah disiapkan dan diintegrasikan.

Jika terjadi masalah atau pertanyaan, silakan hubungi tim pengembang.