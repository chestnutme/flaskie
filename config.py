import os
from ConfigParser import RawConfigParser
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    conf = RawConfigParser()
    conf.read('config.ini')
    SECRET_KEY = conf.get('key', 'SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = conf.get('email', 'MAIL_SERVER')
    MAIL_PORT = conf.get('email', 'MAIL_PORT')
    MAIL_USE_TLS = conf.getboolean('email', 'MAIL_USE_TLS')
    MAIL_USE_SSL = conf.getboolean('email', 'MAIL_USE_SSL')
    MAIL_USERNAME = conf.get('email', 'MAIL_USERNAME')
    MAIL_PASSWORD = conf.get('email', 'MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = conf.get('email', 'FLASKY_MAIL_SUBJECT_PREFIX')
    FLASKY_MAIL_SENDER = conf.get('email', 'FLASKY_MAIL_SENDER')
    FLASKY_ADMIN = conf.get('email', 'FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE=conf.getint('page', 'FLASKY_POSTS_PER_PAGE') or 20

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
