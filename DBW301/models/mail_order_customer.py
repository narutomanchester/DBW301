# coding=utf-8
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .base import TimestampMixin
from . import db

_logger = logging.getLogger(__name__)



class MailOrderCustomer(db.Model, TimestampMixin):
    """
    Contains information of users table
    """
    __tablename__ = 'mail_order_customer'

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), primary_key=True )
    post_address = db.Column(db.String(100), nullable=False)
    time_order = db.Column(db.String(100), nullable=False)

