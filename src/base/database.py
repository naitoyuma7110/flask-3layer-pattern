
from sqlalchemy import create_engine
from sqlalchemy.orm import (scoped_session, sessionmaker, DeclarativeBase)
from flask import Flask, current_app

from base.db.connector import make_session

db_sessions:dict = {}
KEY_DB:str = 'sample'

def init_db(app):
    
    get_session()


def get_session()-> scoped_session:
    '''
    アプリの起動モードに応じて開発、テスト、本番などDBを切り替える
    また、各クライアントに応じたDB接続先などもここで切り替える
    init_app時にconfig.pyに定義されたmodeに応じてapp.configが設定済み
    現状はsampleのみ返す
    '''    
    
    # if current_app.config['ENV'] in ['test']:
    
    return get_sample_session(current_app)

# sampleデータベースとの接続セッションのキャッシュと取得
def get_sample_session(app:Flask) -> scoped_session:
    
    global db_sessions
    
    if KEY_DB in db_sessions:
        return db_sessions[KEY_DB]
    else:
        session = make_session(app)
        db_sessions[KEY_DB] = session
        return session
    
class Base(DeclarativeBase):
    '''
    モデルのBaseクラス
    '''
    pass