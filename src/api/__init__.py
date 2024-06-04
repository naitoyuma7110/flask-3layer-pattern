from flask import Flask
from flask_cors import CORS
from sqlalchemy.orm import scoped_session, sessionmaker
from src.base.database import init_db 
from src.api.routes import init_routes 
from src.config import config_classes

def create_app(mode:str) -> Flask:
    
    app:Flask = init_app(mode)
    
    with app.app_context():
        
        try:
            CORS(app)
            
            init_db(app)
            
            init_routes(app)
        
        except Exception as e:

            raise e

    return app

def init_app(mode) -> Flask:
    app = Flask('api')
    app.config.from_object(config_classes[mode])
    
    return app

def init_logger(mode):
    return
