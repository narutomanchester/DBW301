# coding=utf-8
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .base import TimestampMixin
from . import db

_logger = logging.getLogger(__name__)



class Items(db.Model, TimestampMixin):
    """
    Contains information of users table
    """
    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    manufacturing_time = db.Column(db.String(100), nullable=False)

