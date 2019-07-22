# coding=utf-8
import logging
import logging.config

import flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import os

from config import config

from flask_cors import CORS

__author__ = 'NamTQ'
_logger = logging.getLogger(__name__)

SENTRY_DSN = 'SENTRY_DSN'


def create_app(conf):
    from . import models

    _app = flask.Flask(__name__)
    _app.config.from_object(conf)
    CORS(_app)


    # setup logging
    logging.config.fileConfig(_app.config['LOGGING_CONFIG_FILE'],
                              disable_existing_loggers=False)

    _app.secret_key = conf.FLASK_APP_SECRET_KEY
    models.init_app(_app)

    return _app


app = create_app(config[os.getenv('ENV_MODE', 'develop')])
