from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.species import Species, speciess_schema, species_schema
from app.routes import cache
species_bp = Blueprint("species", __name__)

@species_bp.route("/species", methods=['GET'])
@cache.cached(timeout=60)
def get_species():
    rows = select(Species)

    result = db.session.execute(rows).scalars()
    species = result.all()
    return speciess_schema.dump(species)

@species_bp.route("/species/<int:id>", methods=['GET'])
@cache.memoize(timeout=60)
def get_character_by_id(id):
    row = select(Species).where(Species.id == id)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return species_schema.dump(result)

@species_bp.route("/species/<string:name>", methods=['GET'])
@cache.memoize(timeout=60)
def get_character_by_name(name):
    row = select(Species).where(Species.name == name)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return species_schema.dump(result)