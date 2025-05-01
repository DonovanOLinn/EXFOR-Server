from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.planets import Planets, planets_schema, planet_schema

planets_bp = Blueprint("planets", __name__)

@planets_bp.route("/planets", methods=['GET'])
def get_planets():
    rows = select(Planets)

    result = db.session.execute(rows).scalars()
    planets = result.all()
    return planets_schema.dump(planets)

@planets_bp.route("/planets/<int:planet_id>", methods=['GET'])
def get_character_by_id(planet_id):
    row = select(Planets).where(Planets.planet_id == planet_id)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return planet_schema.dump(result)

@planets_bp.route("/planets/<string:planet_name>", methods=['GET'])
def get_character_by_name(planet_name):
    row = select(Planets).where(Planets.planet_name == planet_name)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return planet_schema.dump(result)