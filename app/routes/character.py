from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.characters import Characters, characters_schema, character_schema
from app.routes import cache
characters_bp = Blueprint("characters", __name__)

@characters_bp.route("/characters", methods=['GET'])
@cache.cached(timeout=60)
def get_characters():
    rows = select(Characters)

    result = db.session.execute(rows).scalars()
    characters = result.all()
    return characters_schema.dump(characters)

@characters_bp.route("/characters/<int:id>", methods=['GET'])
@cache.memoize(timeout=60)
def get_character_by_id(id):
    row = select(Characters).where(Characters.id == id)
    result = db.session.execute(row).scalar_one_or_none()
    character = result
    return character_schema.dump(character)

@characters_bp.route("/characters/<string:name>", methods=['GET'])
@cache.memoize(timeout=60)
def get_character_by_name(name):
    row = select(Characters).where(Characters.name == name)
    result = db.session.execute(row).scalar_one_or_none()
    character = result
    return character_schema.dump(character)