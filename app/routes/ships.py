from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.ships import Ships, ships_schema, ship_schema
from app.routes import cache
ships_bp = Blueprint("ships", __name__)

@ships_bp.route("/ships", methods=['GET'])
@cache.cached(timeout=60)
def get_ships():
    rows = select(Ships)

    result = db.session.execute(rows).scalars()
    ships = result.all()
    return ships_schema.dump(ships)

@ships_bp.route("/ships/<int:id>", methods=['GET'])
@cache.memoize(timeout=60)
def get_character_by_id(id):
    row = select(Ships).where(Ships.id == id)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return ship_schema.dump(result)

@ships_bp.route("/ships/<string:name>", methods=['GET'])
@cache.memoize(timeout=60)
def get_character_by_name(name):
    row = select(Ships).where(Ships.name == name)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return ship_schema.dump(result)