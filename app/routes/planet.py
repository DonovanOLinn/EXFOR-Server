from flask import Blueprint
from sqlalchemy import select
from database import db
from app.models.planets import Planets, planets_schema

planets_bp = Blueprint("planets", __name__)

@planets_bp.route("/planets", methods=['GET'])
def get_planets():
    rows = select(Planets)

    result = db.session.execute(rows).scalars()
    planets = result.all()
    return planets_schema.dump(planets)