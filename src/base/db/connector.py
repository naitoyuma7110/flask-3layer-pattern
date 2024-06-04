from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask
from base.db.connect_info import get_db_connect_info

def make_session(app: Flask):
    # アプリケーションの設定からDB接続情報を取得
    db_url = get_db_connect_info(app)

    # SQLAlchemyのエンジンを作成
    engine = create_engine(db_url)

    # セッションを作成するファクトリを作成
    session_factory = sessionmaker(bind=engine)

    # scoped_sessionを使用してセッションを作成
    session = scoped_session(session_factory, scopefunc=app.app_context)

    return session
