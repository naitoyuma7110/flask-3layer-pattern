from abc import ABC, abstractmethod
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import String, Integer, DateTime, distinct
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm.query import Row
from base.database import Base, get_session


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}  # 既存の定義を拡張
    
    id:Mapped[int] = mapped_column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    username:Mapped[str | None] = mapped_column(String(),  primary_key=False)
    email:Mapped[str | None] = mapped_column(String(),  primary_key=False)
    created_at:Mapped[datetime] = mapped_column(DateTime(), nullable=False, primary_key=False)
    deleted_at:Mapped[datetime | None] = mapped_column(DateTime(), primary_key=False)
    
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=User
        load_instance = True # loadメソッドはモデルインスタンスを返す(デフォルトは辞書型)
        include_fk = True # ↑に加えモデルインスタンスに外部キー情報を保持する

class ISampleRepository(ABC):
    @abstractmethod
    def get_sample_users(self):
        pass
    
class SampleRepository(ISampleRepository):
    
    def get_sample_users(self)-> Row[tuple[int,str,str,datetime,datetime]]:
        
        query_result  = get_session().query(
            distinct(User.id),User.username, User.email, User.created_at, User.deleted_at
        ).all()
        
        return query_result