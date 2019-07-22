# coding=utf-8
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .base import TimestampMixin
from . import db

_logger = logging.getLogger(__name__)



class Customer(db.Model, TimestampMixin):
    """
    Contains information of users table
    """
    __tablename__ = 'customer'

    customer_id = db.Column(db.Integer, primary_key=True )
    customer_name = db.Column(db.String(100), nullable=False)
    city_home_id = db.Column(db.String(50), nullable=False)
    first_order_date = db.Column(db.String(100), nullable=False)


