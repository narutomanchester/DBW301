# coding=utf-8
import logging
import os
from dotenv import load_dotenv
_DOT_ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(_DOT_ENV_PATH)

from DBW301 import app
from DBW301.models.gen_db import GenDB


_logger = logging.getLogger(__name__)


if __name__ == '__main__':
    GenDB()
