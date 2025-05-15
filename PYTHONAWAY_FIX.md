# Cara Mengatasi Error SQLAlchemy di PythonAnywhere

Berikut adalah solusi lengkap untuk mengatasi error berikut di PythonAnywhere:

```
AssertionError: Class <class 'sqlalchemy.sql.elements.SQLCoreOperations'> directly inherits TypingOnly but has additional attributes {'__firstlineno__', '__static_attributes__'}.
```

atau

```
AttributeError: module 'sqlalchemy.orm' has no attribute 'DeclarativeBase'. Did you mean: 'declarative_base'?
```

## SOLUSI LENGKAP (TERBARU)

### 1. File requirements.txt yang Benar

Gunakan file requirements berikut untuk PythonAnywhere:

```
email-validator==2.1.0
flask==3.0.0
flask-dance==7.0.0
flask-login==0.6.3
flask-sqlalchemy==2.5.1  # PENTING: gunakan versi 2.x
gunicorn==23.0.0
matplotlib==3.8.2
mysqlclient==2.1.1
oauthlib==3.2.2
pyjwt==2.8.0
sqlalchemy==1.4.46  # PENTING: gunakan versi 1.4.x
weasyprint==60.2
werkzeug==2.2.3
xhtml2pdf==0.2.11
```

### 2. Perbarui app.py

Ganti kode app.py dengan yang berikut:

```python
import os
import logging
from datetime import datetime
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "kuncirahasiacharlie")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Database configuration - MySQL untuk deployment
database_url = os.environ.get("DATABASE_URL")
if not database_url:
    # Fallback untuk development
    database_url = "sqlite:///kos_management.db"

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    'pool_pre_ping': True,
    "pool_recycle": 300,
}

# Initialize SQLAlchemy with the app - simplified for compatibility
db = SQLAlchemy(app)
```

### 3. Jika Anda Meng-clone Repositori di PythonAnywhere

Jalankan perintah berikut di bash console PythonAnywhere:

```bash
cd ~/sistem-pencatatan-penginapan-kos
python -m venv venv
source venv/bin/activate
pip install flask==3.0.0 flask-sqlalchemy==2.5.1 sqlalchemy==1.4.46
pip install -r requirements_mysql.txt
pip uninstall -y sqlalchemy flask-sqlalchemy
pip install sqlalchemy==1.4.46 flask-sqlalchemy==2.5.1
```

### 4. Edit File WSGI di PythonAnywhere

Pada tab Web > klik WSGI file, dan gunakan kode berikut:

```python
import sys
import os

# Tambahkan direktori proyek ke path sistem
path = '/home/yourusername/sistem-pencatatan-penginapan-kos'
if path not in sys.path:
    sys.path.append(path)

# Atur variabel lingkungan
os.environ['DATABASE_URL'] = 'mysql://yourusername:yourpassword@yourusername.mysql.pythonanywhere-services.com/yourusername$kos_db'
os.environ['SESSION_SECRET'] = 'your_secure_session_key'

# Import aplikasi dari main.py
from main import app as application
```

### 5. Jika Masih Error

Jika masih mengalami error, coba cara berikut:

1. Gunakan Python 3.8 atau 3.9 di PythonAnywhere
2. Hapus cache dan file .pyc:
   ```bash
   find . -name "*.pyc" -delete
   find . -name "__pycache__" -exec rm -rf {} +
   ```
3. Restart aplikasi di PythonAnywhere

---

Catatan: Error ini umum terjadi karena ketidakcocokan SQLAlchemy modern (2.0+) dengan lingkungan Python di PythonAnywhere. Versi Flask-SQLAlchemy 2.x dengan SQLAlchemy 1.4.x adalah kombinasi paling stabil untuk PythonAnywhere.