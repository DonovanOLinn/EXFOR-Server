from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, select, delete
from marshmallow import fields, Schema
from database import db
from models.species import SpeciesSchema, Species

class Ships(db.Model):
    __tablename__ = "ships"
    ship_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ship_name: Mapped[str] = mapped_column(String(255)) 
    ship_type: Mapped[str] = mapped_column(String(255)) 
    status: Mapped[str] = mapped_column(String(255)) 

    species_id: Mapped[int] = mapped_column(Integer, ForeignKey('species.species_id'), unique=True)

    species: Mapped["Species"] = relationship("Species", back_populates='ship')

class ShipsSchema(Schema):
    ship_id = fields.Int(required=False)
    ship_name = fields.Str(required=True)
    ship_type = fields.Str(required=True)
    status = fields.Str(required=True)
    species = fields.Nested(SpeciesSchema)


ship_schema = ShipsSchema()
ships_schema = ShipsSchema(many=True)

