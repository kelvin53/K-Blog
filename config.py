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
    MAIL_USERNAME='kevinkosk23@gmail.com'
    MAIL_PASSWORD ='kipronokelvin'


class DevConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345@localhost/postgres'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345@localhost/postgres'
    pass
    DEBUG = True
configurations = {"development":DevConfig, "production":ProdConfig}
