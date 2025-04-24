from flask import Blueprint
from sqlalchemy import select
from database import db
from app.models.books import Books, books_schema

books_bp = Blueprint("books", __name__)

@books_bp.route("/books", methods=['GET'])
def get_books():
    rows = select(Books)

    result = db.session.execute(rows).scalars()
    books = result.all()
    return books_schema.dump(books)