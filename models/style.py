from app import db, ma

class Style(db.Model):

    __tablename__ = 'styles'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(180), nullable=False)
    shop_logo_img_url = db.Column(db.String(180), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=False)


class StyleSchema(ma.ModelSchema):

    class Meta:
        model = Style
