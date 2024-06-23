import logging
import traceback
import os
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify
from flask_cors import CORS
from src.base.database import init_db 
from src.api.routes import init_routes
from src.api.injector import init_di
from src.config import config_classes

def create_app(mode:str) -> Flask:
    
    init_logger()
    
    logger = logging.getLogger('api')
    logger.info('init logger')

    
    app:Flask = init_app(mode)
    
    with app.app_context():
        
        try:
            CORS(app)
            logger.info('init CORS')
            
            init_db(app)
            logger.info('init db')
            
            init_routes(app)
            logger.info('init routes')
            
            init_filter(app)
            logger.info('init filter')
            
            init_di(app)
            logger.info('init di')
            
            init_error_handler(app)
            logger.info('init error_handler')
        
            
        except Exception as e:
            logger.critical(
                f"init error. error={e}, traceback={traceback.format_exc()}"
            )
            raise e

    return app

def init_app(mode) -> Flask:
    app = Flask('api')
    app.config.from_object(config_classes[mode])
    
    return app

def init_filter(app: Flask):
    from base.filter import api_log_filter
    app.before_request(api_log_filter.before_request)
    app.after_request(api_log_filter.after_request)

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
    
def init_logger():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    log_directory = os.path.join(BASE_DIR, "logs")
    os.makedirs(log_directory, exist_ok=True)  # フォルダが存在しない場合は作成

    # ログファイルのパス
    log_file_path = os.path.join(log_directory, 'app.log')
    # ロガーの設定
    file_handler = RotatingFileHandler(log_file_path, maxBytes=10000, backupCount=3)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')