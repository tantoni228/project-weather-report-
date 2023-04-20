import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    city = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    account_creation_date = sqlalchemy.Column(sqlalchemy.String, default=datetime.datetime.now().strftime('%d:%m:%Y'))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
