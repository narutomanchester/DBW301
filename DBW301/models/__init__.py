# coding=utf-8
import logging

import flask_bcrypt as _fb
import flask_migrate as _fm
import flask_sqlalchemy as _fs
import sys

__author__ = 'NamTQ'
_logger = logging.getLogger(__name__)

db = _fs.SQLAlchemy()
migrate = _fm.Migrate(db=db)
bcrypt = _fb.Bcrypt()

def get_class_by_table_name(table_name):
    for table in db.Model._decl_class_registry.values():
        if hasattr(table, '__tablename__') and table.__tablename__ == table_name:
            return table
    raise Exception('Table does not exist')

def init_app(app, **kwargs):
    """
    Extension initialization point
    :param flask.Flask app:
    :param kwargs:
    :return:
    """
    db.app = app
    db.init_app(app)
    migrate.init_app(app)
    _logger.info('Start app in {env} environment with database: {db}'.format(
        env=app.config['ENV_MODE'],
        db=app.config['SQLALCHEMY_DATABASE_URI']
    ))


from .base import TimestampMixin
from .customer import Customer
from .mail_order_customer import MailOrderCustomer
from .walk_in_customer import WalkInCustomer
from .order import Order
from .ordered_item import OrderedItem
from .items import Items
from .stored_items import StoredItem
from .stores import Stores
from .headquarter import Headquarter
