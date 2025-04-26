from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, String, ForeignKey, select, delete
from marshmallow import fields, Schema
from app.models import db
# from planets import Planets
import datetime
# from .characters import Characters

class Books(db.Model):
    __tablename__ = "books"
    book_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    book_name: Mapped[str] = mapped_column(String(255))
    release_date: Mapped[datetime.date] = mapped_column(Date)
    previous: Mapped[str] = mapped_column(String(255))
    next: Mapped[str] = mapped_column(String(255))
    author_summary: Mapped[str] = mapped_column(String(2048))
    image: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(255))
    narrator: Mapped[str] = mapped_column(String(255))
    run_time: Mapped[str] = mapped_column(String(255))
    
    # planet: Mapped["Planets"] = relationship("Planets", back_populates='first_book_appearance', uselist=True)
    character: Mapped["Characters"] = relationship("Characters", back_populates='first_book_appearance', uselist=True)

class BookSchema(Schema):
    book_id = fields.Int(required=False)
    book_name = fields.Str(required=True)
    release_date = fields.Str(required=True)
    previous = fields.Str(required=True)
    next = fields.Str(required=True)
    author_summary = fields.Str(required=True)
    image = fields.Str(required=True)
    author = fields.Str(required=True)
    narrator = fields.Str(required=True)
    run_time = fields.Str(required=True)

    class Meta: 
        fields = ('book_id', 'book_name', 'release_date', 'previous', 'next', 'author_summary', 'image', 'author', 'narrator', 'run_time')

book_schema = BookSchema()
books_schema = BookSchema(many=True)