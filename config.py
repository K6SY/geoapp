import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app): 
        pass

class DevelopmentConfig(Config):
    ENV='development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'mysql+pymysql://root:Soroc2022@localhost/geoappdev'

class TestingConfig(Config):
    ENV='testing'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'mysql+pymysql://root:Soroc2022@localhost/geoapptest'

class ProductionConfig(Config):
    ENV='production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL') or \
    'mysql+pymysql://root:Soroc2022@localhost/geoappprod'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}