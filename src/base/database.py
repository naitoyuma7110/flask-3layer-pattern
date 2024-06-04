
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask

from base.db.connector import make_session

db_sessions:dict = {}
KEY_DB:str = 'sample'

def init_db(app):
    
    get_session(app)

# sampleデータベースとの接続セッションのキャッシュと取得
def get_session(app:Flask) -> scoped_session:
    
    # DBセッションのキャッシュ
    global db_sessions
    
    if KEY_DB in db_sessions:
        return db_sessions[KEY_DB]
    else:
        session = make_session(app)
        db_sessions[KEY_DB] = session
        return session