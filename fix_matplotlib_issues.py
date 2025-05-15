"""
Script untuk mengatasi masalah RecursionError pada Matplotlib dengan menggunakan Chart.js
"""

import os
import shutil
from pathlib import Path

def apply_chartjs_fixes():
    """Menerapkan perbaikan dengan mengganti fungsi-fungsi yang menggunakan matplotlib"""
    print("Menerapkan perbaikan Chart.js untuk masalah matplotlib...")
    
    # 1. Tambahkan routes_chartjs.py ke main.py
    update_main_py()
    
    # 2. Beritahu pengguna bahwa perbaikan telah diterapkan
    print("Perbaikan berhasil diterapkan!")
    print("Aplikasi sekarang menggunakan Chart.js untuk visualisasi data.")
    print("Restart aplikasi untuk menerapkan perubahan.")

def update_main_py():
    """Update main.py untuk menggunakan Chart.js daripada matplotlib"""
    main_path = Path('main.py')
    
    if not main_path.exists():
        print("Error: File main.py tidak ditemukan!")
        return
    
    # Buat backup dari file asli
    backup_path = Path('main.py.bak')
    shutil.copy2(main_path, backup_path)
    print(f"Backup file asli dibuat: {backup_path}")
    
    # Baca konten main.py
    with open(main_path, 'r') as f:
        content = f.read()
    
    # Cari posisi untuk menambahkan import dari routes_chartjs.py
    if "import routes_chartjs" not in content:
        # Temukan bagian import routes
        import_section = "    # Import routes (setelah app dan db sudah siap)\n    import routes  # noqa: F401"
        
        # Tambahkan import untuk routes_chartjs
        new_import_section = import_section + "\n    # Import Chart.js replacements for matplotlib\n    import routes_chartjs  # noqa: F401 - Pengganti fungsi matplotlib dengan Chart.js"
        
        # Ganti bagian import dengan yang baru
        content = content.replace(import_section, new_import_section)
        
        # Tulis kembali file main.py
        with open(main_path, 'w') as f:
            f.write(content)
            
        print("File main.py berhasil diperbarui.")
    else:
        print("routes_chartjs sudah diimpor dalam main.py.")

if __name__ == "__main__":
    apply_chartjs_fixes()