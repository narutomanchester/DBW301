# coding=utf-8
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .base import TimestampMixin
from . import db

_logger = logging.getLogger(__name__)



class Headquarter(db.Model, TimestampMixin):
    """
    Contains information of users table
    """
    __tablename__ = 'headquarter'

    city_id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100), nullable=True)
    headquarter_addr = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    start_time = db.Column(db.String(100), nullable=True)

