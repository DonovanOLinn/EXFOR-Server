from flask import Blueprint
from sqlalchemy import select
from database import db
from app.models.species import Species, species_schema

species_bp = Blueprint("species", __name__)

@species_bp.route("/species", methods=['GET'])
def get_species():
    rows = select(Species)

    result = db.session.execute(rows).scalars()
    species = result.all()
    return species_schema.dump(species)