from dotenv import load_dotenv
import os


# load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300
