from app import db, ma

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)



class RecipeSchema(ma.ModelSchema):

    class Meta:
        model = Comment
