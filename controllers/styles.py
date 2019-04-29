from flask import Blueprint, request, jsonify, g
from models.style import Style, StyleSchema
from lib.secure_route import secure_route


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


@api.route('/styles', methods=['POST'])
@secure_route
def create():
    style, errors = style_schema.load(request.get_json())
    style.creator = g.current_user

    if errors:
        return jsonify(errors), 422

    style.save()

    return style_schema.jsonify(style)
