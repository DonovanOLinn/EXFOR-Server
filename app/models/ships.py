from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, select, delete
from marshmallow import fields, Schema
from app.models import db
from .species import SpeciesSchema, Species

class Ships(db.Model):
    __tablename__ = "ships"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255)) 
    ship_type: Mapped[str] = mapped_column(String(255)) 
    status: Mapped[str] = mapped_column(String(255)) 

    species_id: Mapped[int] = mapped_column(Integer, ForeignKey('species.id'))

    species: Mapped["Species"] = relationship("Species", back_populates='ship')

class ShipsSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    ship_type = fields.Str(required=True)
    status = fields.Str(required=True)
    species = fields.Nested(SpeciesSchema)


ship_schema = ShipsSchema()
ships_schema = ShipsSchema(many=True)

