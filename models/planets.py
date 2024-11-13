from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, select, delete
from models.books import BookSchema, Books
from marshmallow import fields, Schema
from database import db
import datetime

class Planets(db.Model):
    __tablename__ = "planets"
    planet_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    planet_name: Mapped[str] = mapped_column(String(255))
    planet_nickname: Mapped[str] = mapped_column(String(255))
    # first_book_appearance_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.book_id'), unique=True)
    # Does the Planet & Book relationship need to be one to many?
    # first_book_appearance: Mapped["Books"] = relationship("Books", back_populates="planet")

class PlanetsSchema(Schema):
    planet_id = fields.Int(required=False)
    planet_name = fields.Str(required=True)
    planet_nickname = fields.Str(required=True)
    # first_book_appearance = fields.Nested(BookSchema)

    class Meta: 
        fields = ('planet_id', 'planet_name', 'planet_nickname')
    
planet_schema = PlanetsSchema()
planets_schema = PlanetsSchema(many=True)