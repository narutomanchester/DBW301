# coding=utf-8
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .base import TimestampMixin
from . import db

_logger = logging.getLogger(__name__)



class StoredItem(db.Model, TimestampMixin):
    """
    Contains information of users table
    """
    __tablename__ = 'stored_items'

    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))
    quantity_held = db.Column(db.Integer, nullable=False)
    time_in = db.Column(db.String(100), nullable=False)

