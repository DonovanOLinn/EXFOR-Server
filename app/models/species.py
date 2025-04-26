from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, select, delete
from marshmallow import fields, Schema
from app.models import db
# from .ships import Ships


class Species(db.Model):
    __tablename__ = "species"
    species_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    species_name: Mapped[str] = mapped_column(String(255))
    appearance: Mapped[str] = mapped_column(String(255))
    patron: Mapped[str] = mapped_column(String(255))
    tech_level: Mapped[str] = mapped_column(String(255))
    nickname: Mapped[str] = mapped_column(String(255))
    coalition: Mapped[str] = mapped_column(String(255))
    # Foreign key to Ship
    ship: Mapped["Ships"] = relationship("Ships", back_populates='species', uselist=True)

class SpeciesSchema(Schema):
    species_id = fields.Int(required=False)
    species_name = fields.Str(required=True)
    appearance = fields.Str(required=True)
    patron = fields.Str(required=True)
    tech_level = fields.Str(required=True)
    nickname = fields.Str(required=True)
    coalition = fields.Str(required=True)

    class Meta: 
        fields = ('species_id', 'species_name', 'appearance', 'patron', 'tech_level', 'nickname', 'coalition')

species_schema = SpeciesSchema()
speciess_schema = SpeciesSchema(many=True)