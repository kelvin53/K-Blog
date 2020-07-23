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
    MAIL_PASSWORD = 'kipronokelvin'


class DevConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True
configurations = {"development":DevConfig, "production":ProdConfig}
