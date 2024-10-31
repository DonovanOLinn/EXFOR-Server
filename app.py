from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, 
from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema
import datetime

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow

# Maybe in the future I should adjust this in order to store previous book_id instead of a string to the previous book
class Books(db.Model):
    __tablename__ = "books"
    book_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    book_name: Mapped[str] = mapped_column(String(255))
    release_date: Mapped[datetime.date] = mapped_column(Date)
    previous: Mapped[str] = mapped_column(String(255))
    next: Mapped[str] = mapped_column(String(255))
    author_summary: Mapped[str] = mapped_column(String(255))
    image: Mapped[str] = mapped_column(String(255))
    
    planet: Mapped["Planets"] = relationship("Planets", back_populates='first_book_appearance_id', uselist=True)
    character: Mapped["Characters"] = relationship("Characters", back_populates='first_book_appearance_id', uselist=True)

class BookSchema(Schema):
    book_id = fields.Int(required=False)
    book_name = fields.Str(required=True)
    release_date = fields.Str(required=True)
    previous = fields.Str(required=True)
    next = fields.Str(required=True)
    author_summary = fields.Str(required=True)
    image = fields.Str(required=True)

    class Meta: 
        fields = ('book_id', 'book_name', 'release_date', 'previous', 'next', 'author_summary', 'image')

book_schema = BookSchema()
books_schema = BookSchema(many=True)

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
    ship: Mapped["Ships"] = relationship("Chips", back_populates='species_id', uselist=True)

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

class Planets(db.Model):
    __tablename__ = "planets"
    planet_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    planet_name: Mapped[str] = mapped_column(String(255))
    planet_nickname: Mapped[str] = mapped_column(String(255))
    first_book_appearance_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.book_id'), unique=True)
    # Does the Planet & Book relationship need to be one to many?
    book: Mapped["Books"] = relationship("Books", back_populates="planet")

class PlanetsSchema(Schema):
    planet_id = fields.Int(required=False)
    planet_name = fields.Str(required=True)
    planet_nickname = fields.Str(required=True)
    first_book_appearance_id = fields.Nested(book_schema)

    class Meta: 
        fields = ('planet_id', 'planet_name', 'planet_nickname', 'first_book_appearance_id')
    
planet_schema = PlanetsSchema()
planets_schema = PlanetsSchema(many=True)

class Characters(db.Model):
    __tablename__= "characters"
    character_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    character_name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255))
    last_known_location: Mapped[str] = mapped_column(String(255))
    sex: Mapped[str] = mapped_column(String(255))
    
    # foreign key to book table
    first_book_appearance_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.book_id'), unique=True)

    book: Mapped["Books"] = relationship("Books", back_populates="character")

class CharactersSchema(Schema):
    character_id = fields.Int(required=False)
    character_name = fields.Str(required=True)
    description = fields.Str(required=True)
    status = fields.Str(required=True)
    last_known_location = fields.Str(required=True)
    sex = fields.Str(required=True)
    first_book_appearance_id = fields.Nested(book_schema)

    class Meta: 
        fields = ('character_id', 'character_name', 'description', 'status', 'last_known_location', 'sex', 'first_book_appearance_id')

character_schema = CharactersSchema()
characters_schema = CharactersSchema(many=True)

class Ships(db.Model):
    __tablename__ = "ships"
    ship_id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ship_name = Mapped[str] = mapped_column(String(255)) 
    ship_type = Mapped[str] = mapped_column(String(255)) 
    status = Mapped[str] = mapped_column(String(255)) 

    ship_id: Mapped[int] = mapped_column(Integer, ForeignKey('species.species_id'), unique=True)

    species: Mapped["Species"] = relationship("Species", back_populates='ship')

species_planets_table = db.Table(
    "species_planets_table",
    Base.metadata,
    db.Column("species_id", db.ForeignKey('species.species_id'), primary_key=True),
    db.Column("planets_id", db.ForeignKey('planets.planet_id'), primary_key=True),
    # db.Column
)

