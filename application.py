from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, select, delete
from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema
from app.scrapers.book_scraper import book_scraper
from app.scrapers.species_scraper import species_scraper
from app.scrapers.ship_scraper import ship_scraper
from app.scrapers.planets_scraper import planet_scraper
from app.scrapers.characters_scraper import character_scraper
from database import db
import datetime
from app.models.books import BookSchema, book_schema, books_schema, Books
from app.models.characters import Characters, character_schema, characters_schema, CharactersSchema
from app.models.planets import Planets, planet_schema, planets_schema, PlanetsSchema
from app.models.ships import ship_schema, ships_schema, Ships, ShipsSchema
from app.models.species import species_schema, speciess_schema, Species, SpeciesSchema
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')


class Base(DeclarativeBase):
    pass

db.init_app(app)
ma = Marshmallow


# species_planets_table = db.Table(
#     "species_planets_table",
#     Base.metadata,
#     db.Column("species_id", db.ForeignKey('species.species_id'), primary_key=True),
#     db.Column("planets_id", db.ForeignKey('planets.planet_id'), primary_key=True),
#     # db.Column
# )

@app.route("/")
def home():
    return "Hello world!!"



@app.route("/books", methods=['GET'])
def get_books():
    rows = select(Books)

    result = db.session.execute(rows).scalars()
    books = result.all()
    return books_schema.dump(books)

@app.route("/characters", methods=['GET'])
def get_characters():
    rows = select(Characters)

    result = db.session.execute(rows).scalars()
    characters = result.all()
    return characters_schema.dump(characters)

@app.route("/planets", methods=['GET'])
def get_planets():
    rows = select(Planets)

    result = db.session.execute(rows).scalars()
    planets = result.all()
    return planets_schema.dump(planets)

@app.route("/species", methods=['GET'])
def get_species():
    rows = select(Species)

    result = db.session.execute(rows).scalars()
    species = result.all()
    return speciess_schema.dump(species)

@app.route("/ships", methods=['GET'])
def get_ships():
    rows = select(Ships)

    result = db.session.execute(rows).scalars()
    ships = result.all()
    return ships_schema.dump(ships)


with app.app_context():
    # db.drop_all()
    db.create_all()
    # book_scraper()
    # species_scraper()
    # ship_scraper() # Issue popping up with the ship_scraper. Error at ship_id of 84. Ship Types of Converyance. FK constraint with species.
    # planet_scraper()
    # character_scraper() #Foreign key constraing fails on teh connection with first_book_appearance id


# @app.route("/ships", methods=['GET'])
# def get_ships():
#     rows = select(Ships)

#     result = db.session.execute(rows).scalars()
#     ships = result.all()
#     return ships_schema.dump(ships)

# @app.route("/ships/<int:id>", methods=['GET'])
# def get_single_ship(id):
#     rows = select(Ships).where(Ships.ship_id == id)

#     result = db.session.execute(rows).scalars()