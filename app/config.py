import os


class BaseConfig:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SECRET_KEY = "<SECRET KEY>"
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite3.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf", "txt"}

config = BaseConfig()
