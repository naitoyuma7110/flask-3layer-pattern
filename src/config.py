import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENV = 'product'
    DB_URL = 'postgresql://postgres:postgres@localhost:5433/sample'    
    # SAMPLE_API_PATH = "/sample"
    SAMPLE_API_PATH = os.getenv('SAMPLE_API_PATH')


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_classes = {
    'default':DevelopmentConfig,
    'production':ProductionConfig
}