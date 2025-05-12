from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.planets import Planets, planets_schema, planet_schema
from app.routes import cache
planets_bp = Blueprint("planets", __name__)

@planets_bp.route("/planets", methods=['GET'])
@cache.cached(timeout=60)
def get_planets():
    rows = select(Planets)

    result = db.session.execute(rows).scalars()
    planets = result.all()
    return planets_schema.dump(planets)

@planets_bp.route("/planets/<int:id>", methods=['GET'])
@cache.memoize(timeout=60)
def get_character_by_id(id):
    row = select(Planets).where(Planets.id == id)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return planet_schema.dump(result)

@planets_bp.route("/planets/<string:name>", methods=['GET'])
@cache.memoize(timeout=60)
def get_character_by_name(name):
    row = select(Planets).where(Planets.name == name)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return planet_schema.dump(result)