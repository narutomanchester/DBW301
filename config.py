# coding=utf-8
import logging
from os.path import join, dirname
from dotenv import load_dotenv
import os

__author__ = 'NamTQ'
_logger = logging.getLogger(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
ROOT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__)
))


class Config(object):
    FLASK_APP_SECRET_KEY = os.environ.get('SECRET_KEY') or 'something-very-secret'


    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    ENV_MODE = os.getenv('ENV_MODE', 'develop')

    LOGGING_CONFIG_FILE = os.path.join(ROOT_DIR, 'etc', 'logging.ini')

    SENTRY_DSN = os.environ.get('SENTRY_DSN')




class DevelopmentConfig(Config):
    DEBUG = False
    # SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config = {
    'develop': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
