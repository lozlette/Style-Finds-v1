from app import db, ma
from marshmallow import fields
from .find import Find, FindSchema
from .base import BaseModel, BaseSchema


finds_styles = db.Table(
    'finds_styles',
    db.Column('find_id', db.Integer, db.ForeignKey('finds.id'), primary_key=True),
    db.Column('style_id', db.Integer, db.ForeignKey('styles.id'), primary_key=True)
)

class Style(db.Model, BaseModel):

    __tablename__ = 'styles'

    image_url = db.Column(db.String(180), nullable=False)
    shop_logo_img_url = db.Column(db.String(180), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    finds = db.relationship('Find', backref='styles', secondary='finds_styles', uselist=True)
    find_id = db.Column(db.Integer, db.ForeignKey('finds.id',))



class StyleSchema(ma.ModelSchema, BaseSchema):

    finds = fields.Nested('FindSchema', exclude=('styles',), many=True)

    class Meta:
        model = Style
