from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, select, delete
from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema
from book_scraper import book_scraper
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

# Maybe in the future I should adjust this in order to store previous book_id instead of a string to the previous book
# class Books(db.Model):
#     __tablename__ = "books"
#     book_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     book_name: Mapped[str] = mapped_column(String(255))
#     release_date: Mapped[datetime.date] = mapped_column(Date)
#     previous: Mapped[str] = mapped_column(String(255))
#     next: Mapped[str] = mapped_column(String(255))
#     author_summary: Mapped[str] = mapped_column(String(255))
#     image: Mapped[str] = mapped_column(String(255))
#     author: Mapped[str] = mapped_column(String(255))
#     narrator: Mapped[str] = mapped_column(String(255))
#     run_time: Mapped[str] = mapped_column(String(255))
    
#     planet: Mapped["Planets"] = relationship("Planets", back_populates='first_book_appearance', uselist=True)
#     character: Mapped["Characters"] = relationship("Characters", back_populates='first_book_appearance', uselist=True)

# class BookSchema(Schema):
#     book_id = fields.Int(required=False)
#     book_name = fields.Str(required=True)
#     release_date = fields.Str(required=True)
#     previous = fields.Str(required=True)
#     next = fields.Str(required=True)
#     author_summary = fields.Str(required=True)
#     image = fields.Str(required=True)
#     author = fields.Str(required=True)
#     narrator = fields.Str(required=True)
#     run_time = fields.Str(required=True)

#     class Meta: 
#         fields = ('book_id', 'book_name', 'release_date', 'previous', 'next', 'author_summary', 'image', 'author', 'narrator', 'run_time')

# book_schema = BookSchema()
# books_schema = BookSchema(many=True)

# class Species(db.Model):
#     __tablename__ = "species"
#     species_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     species_name: Mapped[str] = mapped_column(String(255))
#     appearance: Mapped[str] = mapped_column(String(255))
#     patron: Mapped[str] = mapped_column(String(255))
#     tech_level: Mapped[str] = mapped_column(String(255))
#     nickname: Mapped[str] = mapped_column(String(255))
#     coalition: Mapped[str] = mapped_column(String(255))
#     # Foreign key to Ship
#     ship: Mapped["Ships"] = relationship("Ships", back_populates='species', uselist=True)

# class SpeciesSchema(Schema):
#     species_id = fields.Int(required=False)
#     species_name = fields.Str(required=True)
#     appearance = fields.Str(required=True)
#     patron = fields.Str(required=True)
#     tech_level = fields.Str(required=True)
#     nickname = fields.Str(required=True)
#     coalition = fields.Str(required=True)

#     class Meta: 
#         fields = ('species_id', 'species_name', 'appearance', 'patron', 'tech_level', 'nickname', 'coalition')

# species_schema = SpeciesSchema()
# speciess_schema = SpeciesSchema(many=True)

# class Planets(db.Model):
#     __tablename__ = "planets"
#     planet_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     planet_name: Mapped[str] = mapped_column(String(255))
#     planet_nickname: Mapped[str] = mapped_column(String(255))
#     first_book_appearance_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.book_id'), unique=True)
#     # Does the Planet & Book relationship need to be one to many?
#     first_book_appearance: Mapped["Books"] = relationship("Books", back_populates="planet")

# class PlanetsSchema(Schema):
#     planet_id = fields.Int(required=False)
#     planet_name = fields.Str(required=True)
#     planet_nickname = fields.Str(required=True)
#     first_book_appearance = fields.Nested(BookSchema)

#     class Meta: 
#         fields = ('planet_id', 'planet_name', 'planet_nickname', 'first_book_appearance')
    
# planet_schema = PlanetsSchema()
# planets_schema = PlanetsSchema(many=True)

# class Characters(db.Model):
#     __tablename__= "characters"
#     character_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     character_name: Mapped[str] = mapped_column(String(255))
#     description: Mapped[str] = mapped_column(String(255))
#     status: Mapped[str] = mapped_column(String(255))
#     last_known_location: Mapped[str] = mapped_column(String(255))
#     sex: Mapped[str] = mapped_column(String(255))
    
#     # foreign key to book table
#     first_book_appearance_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.book_id'), unique=True)
#     first_book_appearance: Mapped["Books"] = relationship("Books", back_populates="character")

#     # book: Mapped["Books"] = relationship("Books", back_populates="character")

# class CharactersSchema(Schema):
#     character_id = fields.Int(required=False)
#     character_name = fields.Str(required=True)
#     description = fields.Str(required=True)
#     status = fields.Str(required=True)
#     last_known_location = fields.Str(required=True)
#     sex = fields.Str(required=True)
#     first_book_appearance = fields.Nested(BookSchema)

#     class Meta: 
#         fields = ('character_id', 'character_name', 'description', 'status', 'last_known_location', 'sex', 'first_book_appearance')

# character_schema = CharactersSchema()
# characters_schema = CharactersSchema(many=True)

# class Ships(db.Model):
#     __tablename__ = "ships"
#     ship_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     ship_name: Mapped[str] = mapped_column(String(255)) 
#     ship_type: Mapped[str] = mapped_column(String(255)) 
#     status: Mapped[str] = mapped_column(String(255)) 

#     species_id: Mapped[int] = mapped_column(Integer, ForeignKey('species.species_id'), unique=True)

#     species: Mapped["Species"] = relationship("Species", back_populates='ship')

# class ShipsSchema(Schema):
#     ship_id = fields.Int(required=False)
#     ship_name = fields.Str(required=True)
#     ship_type = fields.Str(required=True)
#     status = fields.Str(required=True)
#     species = fields.Nested(SpeciesSchema)


# ship_schema = ShipsSchema()
# ships_schema = ShipsSchema(many=True)

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
    book_scraper()


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