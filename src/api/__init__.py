from flask import Flask
from flask_cors import CORS
from sqlalchemy.orm import scoped_session, sessionmaker
from src.base.database import init_db 


def create_app():

    app:Flask = init_app()


    with app.app_context():
        
        try:
            CORS(app)
            
            # 初期化処理
            init_db(app)
        
        except Exception as e:

            raise e
        
        

    return app

def init_app() -> Flask:
    app = Flask('api')
    
    return app

