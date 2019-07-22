# coding=utf-8
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .base import TimestampMixin
from . import db

_logger = logging.getLogger(__name__)



class OrderedItem(db.Model, TimestampMixin):
    """
    Contains information of users table
    """
    __tablename__ = 'ordered_item'

    order_no = db.Column(db.Integer, db.ForeignKey('order.order_no'), primary_key=True )
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'), nullable=False)
    quantity_ordered = db.Column(db.Integer, nullable=False)
    ordered_price = db.Column(db.Float, nullable=False)
    time_order = db.Column(db.String(100), nullable=False)

