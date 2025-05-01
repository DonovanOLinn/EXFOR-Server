from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.species import Species, speciess_schema, species_schema

species_bp = Blueprint("species", __name__)

@species_bp.route("/species", methods=['GET'])
def get_species():
    rows = select(Species)

    result = db.session.execute(rows).scalars()
    species = result.all()
    return speciess_schema.dump(species)

@species_bp.route("/species/<int:species_id>", methods=['GET'])
def get_character_by_id(species_id):
    row = select(Species).where(Species.species_id == species_id)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return species_schema.dump(result)

@species_bp.route("/species/<string:species_name>", methods=['GET'])
def get_character_by_name(species_name):
    row = select(Species).where(Species.species_name == species_name)
    result = db.session.execute(row).scalar_one_or_none()
    # character = result
    return species_schema.dump(result)