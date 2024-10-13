class BaseConfig:
    SECRET_KEY = "<SECRET KEY>"
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite3.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

config = BaseConfig()
