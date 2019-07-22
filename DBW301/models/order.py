# coding=utf-8
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .base import TimestampMixin
from . import db

_logger = logging.getLogger(__name__)



class Order(db.Model, TimestampMixin):
    """
    Contains information of users table
    """
    __tablename__ = 'order'

    order_no = db.Column(db.Integer, primary_key=True )
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    order_date = db.Column(db.String(100), nullable=False)

