from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.characters import Characters, characters_schema

characters_bp = Blueprint("characters", __name__)

@characters_bp.route("/characters", methods=['GET'])
def get_characters():
    rows = select(Characters)

    result = db.session.execute(rows).scalars()
    characters = result.all()
    return characters_schema.dump(characters)