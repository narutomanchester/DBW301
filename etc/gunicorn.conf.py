# coding=utf-8
import logging
import multiprocessing
import os

__author__ = 'NamTQ'
_logger = logging.getLogger(__name__)

_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..',
))
_VAR = os.path.join(_ROOT, 'var')
_ETC = os.path.join(_ROOT, 'etc')

bind = '0.0.0.0:5000'
reload = True

workers = multiprocessing.cpu_count() * 2 + 1
# workers = 3
timeout = 180  # 3 minutes
keepalive = 24 * 3600  # 1 day
logconfig = os.path.join(_ETC, 'logging.ini')
