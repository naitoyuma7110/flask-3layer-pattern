from flask import Flask, jsonify
from flask_cors import CORS
from src.base.database import init_db 
from src.api.routes import init_routes
from src.api.injector import init_di
from src.config import config_classes

def create_app(mode:str) -> Flask:
    
    app:Flask = init_app(mode)
    
    with app.app_context():
        
        try:
            
            init_db(app)
            
            init_routes(app)
            
            init_di(app)
            
            init_error_handler(app)
        
            CORS(app)
            
        except Exception as e:

            raise e

    return app

def init_app(mode) -> Flask:
    app = Flask('api')
    app.config.from_object(config_classes[mode])
    
    return app

def init_logger(mode):
    return

def init_error_handler(app: Flask):
    from base.exception import (InvalidParametersError, UriNotFoundError)
    from base.response import (response_error_params, response_error_notfound)
    
    @app.errorhandler(404)
    def page_not_found(error):
        response = {
            "title": "指定されたURLは存在しません",
            "type": "uri-not-found",
            "status": 404
        }
        return jsonify(response), 404
    
    # 404 エラーをキャッチしてカスタム例外に置き換える
    @app.errorhandler(404)
    def handle_404_error(error):

        return response_error_notfound(error)
    
    app.register_error_handler(InvalidParametersError, response_error_params)    
    app.register_error_handler(UriNotFoundError,response_error_notfound)