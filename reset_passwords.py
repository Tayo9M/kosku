import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import DeclarativeBase

# Inisialisasi Flask dan database
class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    'pool_pre_ping': True,
    "pool_recycle": 300,
}

db = SQLAlchemy(app, model_class=Base)

# Import model User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='user')
    location = db.Column(db.String(100))

def reset_all_passwords():
    """Reset semua password pengguna dengan password default dan
    menggunakan metode hashing yang kompatibel (pbkdf2:sha256)"""
    
    # Default password untuk setiap pengguna (username + '123')
    with app.app_context():
        users = User.query.all()
        for user in users:
            default_password = f"{user.username}123"
            # Gunakan pbkdf2:sha256 yang kompatibel dengan Python 3.9
            user.password_hash = generate_password_hash(default_password, method='pbkdf2:sha256')
            print(f"Reset password untuk {user.username} (peran: {user.role})")
        
        # Commit perubahan ke database
        db.session.commit()
        print("Semua password telah di-reset!")
        print("Password default: [nama_pengguna]123 (contoh: admin123, manager1123, staff1123, dll)")

if __name__ == "__main__":
    reset_all_passwords()