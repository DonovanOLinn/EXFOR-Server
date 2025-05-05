from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, select, delete
from marshmallow import fields, Schema
from app.models import db

from app.models.books import BookSchema, Books

class Characters(db.Model):
    __tablename__= "characters"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(5000))
    status: Mapped[str] = mapped_column(String(255))
    last_known_location: Mapped[str] = mapped_column(String(255))
    sex: Mapped[str] = mapped_column(String(255))
    
    # foreign key to book table
    first_book_appearance_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.id'))
    first_book_appearance: Mapped["Books"] = relationship("Books", back_populates="character")

    # book: Mapped["Books"] = relationship("Books", back_populates="character")

class CharactersSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    status = fields.Str(required=True)
    last_known_location = fields.Str(required=True)
    sex = fields.Str(required=True)
    first_book_appearance = fields.Nested(BookSchema)

    class Meta: 
        fields = ('id', 'name', 'description', 'status', 'last_known_location', 'sex', 'first_book_appearance')

character_schema = CharactersSchema()
characters_schema = CharactersSchema(many=True)