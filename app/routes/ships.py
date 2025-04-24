from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.ships import Ships, ships_schema

ships_bp = Blueprint("ships", __name__)

@ships_bp.route("/ships", methods=['GET'])
def get_ships():
    rows = select(Ships)

    result = db.session.execute(rows).scalars()
    ships = result.all()
    return ships_schema.dump(ships)