import os
from dotenv import load_dotenv
import message_config 

load_dotenv()

class Config:
    ENV = 'product'
    DB_URL = 'postgresql://postgres:postgres@localhost:5433/sample'    
    
    SAMPLE_API_PATH = os.getenv('SAMPLE_API_PATH')
    
    ERROR_RESPONSE = message_config.ERROR_RESPONSE


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    
class UnittestConfig(Config):
    ENV = 'unittest'
    DEBUG = True

config_classes = {
    'default':DevelopmentConfig,
    'production':ProductionConfig,
    'unittest':UnittestConfig
}