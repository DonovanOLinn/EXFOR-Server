from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, select, delete
from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema
from scrapers.book_scraper import book_scraper
from scrapers.species_scraper import species_scraper
from scrapers.ship_scraper import ship_scraper
from database import db
import datetime
from models.books import BookSchema, book_schema, books_schema, Books
from models.characters import Characters, character_schema, characters_schema, CharactersSchema
from models.planets import Planets, planet_schema, planets_schema, PlanetsSchema
from models.ships import ship_schema, ships_schema, Ships, ShipsSchema
from models.species import species_schema, speciess_schema, Species, SpeciesSchema


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:CodingTemple@localhost/expeditionary_force"


class Base(DeclarativeBase):
    pass

# db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow


species_planets_table = db.Table(
    "species_planets_table",
    Base.metadata,
    db.Column("species_id", db.ForeignKey('species.species_id'), primary_key=True),
    db.Column("planets_id", db.ForeignKey('planets.planet_id'), primary_key=True),
    # db.Column
)

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
    ship_scraper()


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