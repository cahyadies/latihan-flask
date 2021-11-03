from app import routes  # Memanggil file routes (akan segera dibuat)
from flask import Flask  # Memanggil library Flask

# Untuk menjelaskan nama modul yang digunakan, sehingga ketika folder lain memanggil folder app akan otomatis teridentifikasi.
app = Flask(__name__)
