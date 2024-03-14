"""test for database.py"""

from unittest.mock import patch, MagicMock
import pytest
from database import (
    Book,
    add_book,
    get_books,
    get_book,
    update_book,
    delete_book,
    search_books_by_title_or_author,
)
from app import app


class TestDatabaseOperations:
    """TestDatabase class

    This class represents a test database.

    """

    @pytest.fixture(autouse=True)
    def setup_app_context(self):
        """Setup and teardown the Flask application context for each test."""
        with app.app_context():
            yield

    @pytest.fixture(name="mock_db_session")
    def mock_db_session_fixture(self):
        """Fixture to mock the database session add and commit methods."""
        with patch("database.db.session.add") as mock_add, patch(
            "database.db.session.commit"
        ) as mock_commit:
            yield mock_add, mock_commit

    def test_add_book(self, mock_db_session):
        """Test adding a book to the database."""
        # Given
        title = "Test Book"
        author = "Test Author"
        mock_add, mock_commit = mock_db_session

        # Mock the Book object to avoid database interactions
        mock_book = MagicMock(spec=Book, title=title, author=author)

        with patch("database.Book", return_value=mock_book):
            # When
            result = add_book(title, author)

            # Then
            assert result.title == title
            assert result.author == author
            mock_add.assert_called_once_with(mock_book)
            mock_commit.assert_called_once()

    def test_get_books(self):
        """Test getting all books from the database."""
        # Given
        mock_book1 = MagicMock(spec=Book, id=1, title="Book 1", author="Author 1")
        mock_book2 = MagicMock(spec=Book, id=2, title="Book 2", author="Author 2")
        expected_books = [mock_book1, mock_book2]

        with patch("database.Book.query") as mock_query:
            mock_query.all.return_value = expected_books

            # When
            result = get_books()

            # Then
            assert result == expected_books
            mock_query.all.assert_called_once()

    def test_get_book(self):
        """Test getting a single book by ID from the database."""
        # Given
        book_id = 1
        mock_book = MagicMock(
            spec=Book, id=book_id, title="Test Book", author="Test Author"
        )

        with patch("database.Book.query") as mock_query:
            mock_query.get_or_404.return_value = mock_book

            # When
            result = get_book(book_id)

            # Then
            assert result == mock_book
            mock_query.get_or_404.assert_called_once_with(book_id)

    def test_update_book(self):
        """Test updating a book in the database."""
        # Given
        book_id = 1
        new_title = "Updated Title"
        new_author = "Updated Author"
        mock_book = MagicMock(
            spec=Book, id=book_id, title="Old Title", author="Old Author"
        )

        with patch("database.get_book", return_value=mock_book), patch(
            "database.db.session.commit"
        ) as mock_commit:

            # When
            result = update_book(book_id, new_title, new_author)

            # Then
            assert result.title == new_title
            assert result.author == new_author
            mock_commit.assert_called_once()

    def test_delete_book(self):
        """Test deleting a book from the database."""
        # Given
        book_id = 1
        mock_book = MagicMock(spec=Book, id=book_id)

        with patch("database.get_book", return_value=mock_book), patch(
            "database.db.session.delete"
        ) as mock_delete, patch("database.db.session.commit") as mock_commit:

            # When
            result = delete_book(book_id)

            # Then
            assert result is True
            mock_delete.assert_called_once_with(mock_book)
            mock_commit.assert_called_once()

    def test_search_books_by_title_or_author(self):
        """test for searching books by author"""
        # Given
        search_term = "Test"
        mock_book = MagicMock(spec=Book, id=1, title="Test Book", author="Test Author")
        expected_books = [mock_book]

        with patch("database.Book.query") as mock_query:
            mock_query.filter.return_value.all.return_value = expected_books

            # When
            result = search_books_by_title_or_author(search_term)

            # Then
            assert result == expected_books
