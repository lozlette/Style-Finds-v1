from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow_sqlalchemy.fields import Nested


class Find(db.Model, BaseModel):

    __tablename__ = 'finds'

    image_url = db.Column(db.String(180), nullable=False)
    shop_logo_img_url = db.Column(db.String(180), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(1000), nullable=False)



class FindSchema(ma.SQLAlchemySchema, BaseSchema):

    styles = fields.Nested('StyleSchema', exclude=('finds',), many=True)

    class Meta:
        model = Find
