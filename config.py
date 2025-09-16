import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-secreta')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:password@localhost/club_deportivo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
