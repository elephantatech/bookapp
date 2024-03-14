""" database.py"""
import logging
from typing import List, Optional
from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)

db = SQLAlchemy()


class Book(db.Model):
    """
    Book model for representing books in the database.
    """

    __tablename__ = "books"
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(100), nullable=False)
    author: str = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        """Provides a readable representation of a Book instance."""
        return f"<Book {self.title}>"


def add_book(title: str, author: str) -> Book:
    """
    Adds a new book to the database.

    :param title: Title of the book.
    :param author: Author of the book.
    :return: The newly created Book object.
    """
    new_book = Book(title=title, author=author)
    db.session.add(new_book)
    db.session.commit()
    logger.info(
        "Book added: %s by %s",
        new_book.title,
        new_book.author,
        extra={"book_title": new_book.title, "book_author": new_book.author},
    )
    return new_book


def get_books() -> List[Book]:
    """
    Retrieves all books from the database.

    :return: A list of Book objects.
    """
    return Book.query.all()


def get_book(book_id: int) -> Optional[Book]:
    """
    Retrieves a book by its ID from the database.

    :param book_id: The ID of the book to retrieve.
    :return: A Book object.
    """
    return Book.query.get_or_404(book_id)


def update_book(book_id: int, title: str, author: str) -> Book:
    """
    Updates the details of an existing book.

    :param book_id: The ID of the book to update.
    :param title: The new title of the book.
    :param author: The new author of the book.
    :return: The updated Book object.
    """
    book = get_book(book_id)

    book.title = title
    book.author = author
    db.session.commit()
    logger.info("Updating Book with %s title %s and author %s", book_id, title, author)
    return book


def delete_book(book_id: int) -> bool:
    """
    Deletes a book from the database.

    :param book_id: The ID of the book to delete.
    :return: True if the operation was successful.
    """
    book = get_book(book_id)
    db.session.delete(book)
    db.session.commit()
    logger.info(
        "Book deleted: %s", book.title, extra={"id": book_id, "book_title": book.title}
    )
    return True


def search_books_by_title_or_author(search_term: str) -> List[Book]:
    """
    Searches for books by title or author.

    :param search_term: The search query for book title or author.
    :return: A list of Book objects that match the search term.
    """

    search = f"%{search_term}%"
    books = Book.query.filter(
        db.or_(Book.title.ilike(search), Book.author.ilike(search))
    ).all()
    return books
