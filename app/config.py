import os


class BaseConfig:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SECRET_KEY = "<SECRET KEY>"
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite3.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf", "txt"}
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587 # обычно это 587 для TLS или 465 для SSL
    
    # Настройки email для отправки через Gmail
    MAIL_USERNAME = 'akromjonrustamov56@gmail.com'
    MAIL_PASSWORD = 'frcygugpgjcehvnf'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'akromjonrustamov56@gmail.com'
    
    # Замените на ваш Redis URI
    CELERY_BROKER_URL = 'sqla+sqlite:///tasks.sqlite'
    CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'UTC'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite3.db"


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = DevelopmentConfig()
