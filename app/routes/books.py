from flask import Blueprint
from sqlalchemy import select
from app.models import db
from app.models.books import Books, books_schema, book_schema
from app.routes import cache


books_bp = Blueprint("books", __name__)

@books_bp.route("/books", methods=['GET'])
@cache.cached(timeout=60)
def get_books():
    rows = select(Books)

    result = db.session.execute(rows).scalars()
    books = result.all()
    return books_schema.dump(books)

@books_bp.route("/books/<int:id>", methods=['GET'])
@cache.memoize(timeout=60)
def get_book_by_id(id):
    row = select(Books).where(Books.id == id)
    result = db.session.execute(row).scalar_one_or_none()
    book = result
    return book_schema.dump(book)

@books_bp.route("/books/<string:name>", methods=['GET'])
@cache.memoize(timeout=60)
def get_book_by_name(name):
    row = select(Books).where(Books.name == name)
    result = db.session.execute(row).scalar_one_or_none()
    book = result
    return book_schema.dump(book)