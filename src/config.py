import os

class Config:
    ENV = 'product'
    
    DB_URL = 'postgresql://postgres:postgres@localhost:5433/sample'    
    SAMPLE_API_PATH = "sample"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_classes = {
    'default':DevelopmentConfig,
    'production':ProductionConfig
}