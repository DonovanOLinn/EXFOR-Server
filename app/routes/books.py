from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.books import Books, books_schema, book_schema

books_bp = Blueprint("books", __name__)

@books_bp.route("/books", methods=['GET'])
def get_books():
    rows = select(Books)

    result = db.session.execute(rows).scalars()
    books = result.all()
    return books_schema.dump(books)

@books_bp.route("/books/<int:book_id>", methods=['GET'])
def get_book_by_id(book_id):
    row = select(Books).where(Books.book_id == book_id)
    result = db.session.execute(row).scalar_one_or_none()
    book = result
    return book_schema.dump(book)

@books_bp.route("/books/<string:book_name>", methods=['GET'])
def get_book_by_name(book_name):
    row = select(Books).where(Books.book_name == book_name)
    result = db.session.execute(row).scalar_one_or_none()
    book = result
    return book_schema.dump(book)