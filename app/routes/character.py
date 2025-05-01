from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.characters import Characters, characters_schema, character_schema

characters_bp = Blueprint("characters", __name__)

@characters_bp.route("/characters", methods=['GET'])
def get_characters():
    rows = select(Characters)

    result = db.session.execute(rows).scalars()
    characters = result.all()
    return characters_schema.dump(characters)

@characters_bp.route("/characters/<int:character_id>", methods=['GET'])
def get_character_by_id(character_id):
    row = select(Characters).where(Characters.character_id == character_id)
    result = db.session.execute(row).scalar_one_or_none()
    character = result
    return character_schema.dump(character)

@characters_bp.route("/characters/<string:character_name>", methods=['GET'])
def get_character_by_name(character_name):
    row = select(Characters).where(Characters.character_name == character_name)
    result = db.session.execute(row).scalar_one_or_none()
    character = result
    return character_schema.dump(character)