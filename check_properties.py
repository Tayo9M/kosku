from app import app, db
from models import Property

with app.app_context():
    properties = Property.query.all()
    if properties:
        print("Data properti:")
        for p in properties:
            print(f"ID: {p.id}, Nama: {p.name}")
    else:
        print("Tidak ada data properti")
