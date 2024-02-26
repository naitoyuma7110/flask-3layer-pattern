from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# PostgreSQLの接続情報を設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5433/sample'

# SQLAlchemyの初期化
db = SQLAlchemy(app)

# データベースモデルの定義
class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.SERIAL, primary_key=True, autoincrement=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)

# アプリケーションコンテキスト内でデータベースの操作を行う
# ユーザー名が存在しない場合のみデータを挿入
def insert_user_if_not_exists(username, email):
	try: 
		# 処理内容
		if not User.query.filter_by(username=username).first():
			new_user = User(username=username, email=email)
			db.session.add(new_user) 
		else:
			print(f"User '{username}' already exists.")
		db.session.commit()
	except Exception:
		db.session.rollback() 
		# raiseでExceptionを返す
		raise

with app.app_context():
	# データを挿入
	insert_user_if_not_exists('john_doe', 'john@example.com')
	insert_user_if_not_exists('jane_smith', 'jane@example.com')

@app.route('/')
def index():
	# SQLAlchemyのモデルを使用しUserテーブルから全レコードを取得
	users = User.query.all()
	user_list = []
	for user in users:
			user_data = {
					'id': user.id,
					'username': user.username,
					'email': user.email
			}
			user_list.append(user_data)
	# リスト化してjsonで返す
	return jsonify(user_list)

if __name__ == '__main__':
	app.run(debug=True)
