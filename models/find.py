from app import db, ma

class Find(db.Model):

    __tablename__ = 'finds'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(180), nullable=False)
    shop_logo_img_url = db.Column(db.String(180), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(1000), nullable=False)


class FindSchema(ma.ModelSchema):

    class Meta:
        model = Find
