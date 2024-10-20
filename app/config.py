import os

from dotenv import load_dotenv


class BaseConfig:
    load_dotenv()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv("DEBUG", True)
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf", "txt"}
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587  # обычно это 587 для TLS или 465 для SSL

    # configure email to optimzate Gmail
    MAIL_USERNAME = os.getenv("EMAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = "akromjonrustamov56@gmail.com"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite3.db"


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

config = DevelopmentConfig()
