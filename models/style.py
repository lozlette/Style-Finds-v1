from app import db, ma
from marshmallow import fields
from .find import Find, FindSchema



class Style(db.Model):

    __tablename__ = 'styles'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(180), nullable=False)
    shop_logo_img_url = db.Column(db.String(180), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    finds = db.relationship('Find', backref='styles')
    find_id = db.Column(db.Integer, db.ForeignKey('finds.id'))



class StyleSchema(ma.ModelSchema):

    finds = fields.Nested('FindSchema', many=True, exclude='styles',)

    class Meta:
        model = Style
