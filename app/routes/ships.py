from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.ships import Ships, ships_schema, ship_schema

ships_bp = Blueprint("ships", __name__)

@ships_bp.route("/ships", methods=['GET'])
def get_ships():
    rows = select(Ships)

    result = db.session.execute(rows).scalars()
    ships = result.all()
    return ships_schema.dump(ships)

@ships_bp.route("/ships/<int:ship_id>", methods=['GET'])
def get_character_by_id(ship_id):
    row = select(Ships).where(Ships.ship_id == ship_id)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return ship_schema.dump(result)

@ships_bp.route("/ships/<string:ship_name>", methods=['GET'])
def get_character_by_name(ship_name):
    row = select(Ships).where(Ships.ship_name == ship_name)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return ship_schema.dump(result)