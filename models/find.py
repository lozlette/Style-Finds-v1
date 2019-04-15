from app import db, ma

class Find(db.Model):

    __tablename__ = 'finds'

    id = db.Column(db.Integer, primary_key=True)



class RecipeSchema(ma.ModelSchema):

    class Meta:
        model = Find
