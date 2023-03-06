from marshmallow import Schema, fields
from config_db import db

class FrameworkModel(db.Model):
    """
    Модель для таблицы FrameworkModel
    """
    __tablename__ = 'framework_model'
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    language = db.Column(db.String(255))

class FrameworkModelSchema(Schema):
    """
    Schema для модели FrameworkModel
    """
    pk = fields.Int(dump_only=True)
    name = fields.Str()
    language = fields.Str()
