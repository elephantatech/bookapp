"""
This module defines the Flask application and its routes.

It includes routes for adding, retrieving, updating, and deleting books,
as well as searching for books by title or author.
"""

import logging.config
from flask import Flask, request, jsonify
from database import (
    db,
    add_book,
    get_books,
    get_book,
    update_book,
    delete_book,
    search_books_by_title_or_author,
)
from settings import settings

logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# add database connection string
app.config["SQLALCHEMY_DATABASE_URI"] = settings.sqlalchemy_database_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# Creates the database tables before the first request is processed.
# with app.app_context():
#     db.create_all()


@app.route("/books", methods=["POST"])
def add_book_route():
    """
    API endpoint to add a new book.
    Expects a JSON payload with 'title' and 'author'.
    """
    data = request.get_json()
    book = add_book(title=data["title"], author=data["author"])
    return (
        jsonify(
            {
                "message": "Book added successfully",
                "book": {"id": book.id, "title": book.title, "author": book.author},
            }
        ),
        201,
    )


@app.route("/books", methods=["GET"])
def get_books_route():
    """API endpoint to retrieve all books."""
    books = get_books()
    return jsonify(
        [{"id": book.id, "title": book.title, "author": book.author} for book in books]
    )


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book_route(book_id):
    """
    API endpoint to retrieve a single book by its ID.
    """
    book = get_book(book_id)
    return jsonify({"id": book.id, "title": book.title, "author": book.author})


@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book_route(book_id):
    """
    API endpoint to update an existing book.
    Expects a JSON payload with 'title' and 'author'.
    """
    data = request.get_json()
    book = update_book(book_id=book_id, title=data["title"], author=data["author"])
    return jsonify(
        {
            "message": "Book updated successfully",
            "book": {"id": book.id, "title": book.title, "author": book.author},
        }
    )


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book_route(book_id):
    """
    API endpoint to delete a book by its ID.
    """
    delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"})


@app.route("/search", methods=["GET"])
def search_books():
    """
    API endpoint to search for books by string that is in title or author.
    """
    search_term = request.args.get("search", "")
    if not search_term:
        return jsonify({"error": "Please provide a search term"}), 400

    books = search_books_by_title_or_author(search_term)

    if books:
        return jsonify(
            [
                {"id": book.id, "title": book.title, "author": book.author}
                for book in books
            ]
        )
    else:
        return jsonify({"message": "No books found matching the search criteria"}), 404


@app.errorhandler(404)
def resource_not_found(e):
    """Custom error handler for 404 errors."""
    return jsonify(error=str(e), message="Resource not found."), 404


if __name__ == "__main__":
    app.run(debug=True)
