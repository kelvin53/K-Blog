import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    Debug = True
    SECRET_KEY= '4444'
    UPLOADED_PHOTOS_DEST = 'app/static/images'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME='ijanemercy@gmail.com'
    MAIL_PASSWORD = '@janeMercy700'


class DevConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345@localhost/postgres'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345@localhost/postgres'
    pass
configurations = {"development":DevConfig, "production":ProdConfig}
