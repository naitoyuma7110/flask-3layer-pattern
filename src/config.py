import os

class Config:
    SECRET_KEY = os.urandom(24)
    DB_URL = 'postgresql://postgres:postgres@localhost:5433/sample'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SAMPLE_API_PATH = "sample"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_classes = {
    'default':DevelopmentConfig,
    'production':ProductionConfig
}