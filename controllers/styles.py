from flask import Blueprint, request, jsonify, g
from models.style import Style, StyleSchema

api = Blueprint('styles', __name__)


styles_schema = StyleSchema(many=True)
style_schema = StyleSchema()

@api.route('/styles', methods=['GET'])
def index():
    styles = Style.query.all()
    return styles_schema.jsonify(styles)

@api.route('/styles/<int:style_id>', methods=['GET'])
# @secure_route
def show(style_id):
    style = Style.query.get(style_id)
    return style_schema.jsonify(style)
