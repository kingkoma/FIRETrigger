from .base import Config


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    LOG_LEVEL = "DEBUG"
