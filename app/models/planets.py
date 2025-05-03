from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, select, delete
from marshmallow import fields, Schema
from app.models import db

class Planets(db.Model):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    planet_nickname: Mapped[str] = mapped_column(String(255))
    # first_book_appearance_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.book_id'), unique=True)
    # Does the Planet & Book relationship need to be one to many?
    # first_book_appearance: Mapped["Books"] = relationship("Books", back_populates="planet")

class PlanetsSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    planet_nickname = fields.Str(required=True)
    # first_book_appearance = fields.Nested(BookSchema)

    class Meta: 
        fields = ('id', 'name', 'planet_nickname')
    
planet_schema = PlanetsSchema()
planets_schema = PlanetsSchema(many=True)