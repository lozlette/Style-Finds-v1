# from app import db, ma
#
# class User(db.Model):
#
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     name = db.Column(db.String(100))
#     image_url = db.Column(db.String(180))
#     bio = db.Column(db.String(250), nullable=False)
#     email = db.Column(db.String(180), nullable=False)
#     password_hash = db.Column(db.String(128), nullable=True)
#
#
# class RecipeSchema(ma.ModelSchema):
#
#     class Meta:
#         model = User
