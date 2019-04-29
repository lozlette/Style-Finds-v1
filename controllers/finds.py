from flask import Blueprint, request, jsonify, g
from models.find import Find, FindSchema

api = Blueprint('finds', __name__)


finds_schema = FindSchema(many=True)
find_schema = FindSchema()

@api.route('/finds', methods=['GET'])
def index():
    finds = Find.query.all()
    return finds_schema.jsonify(finds)

@api.route('/finds/<int:find_id>', methods=['GET'])
# @secure_route
def show(find_id):
    find = Find.query.get(find_id)
    return find_schema.jsonify(find)
