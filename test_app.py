"""Test Flask application."""

from unittest.mock import patch
import pytest
from app import app
from database import Book


@pytest.fixture(name="client")
def test_client():
    """Create test client."""
    with app.test_client() as client:
        yield client


def test_add_book_route(client):
    """Test add book route."""
    with patch("app.add_book") as mock_add_book:
        mock_add_book.return_value = Book(id=1, title="Test Book", author="Test Author")
        response = client.post(
            "/books", json={"title": "Test Book", "author": "Test Author"}
        )

        assert response.status_code == 201
        assert b"Book added successfully" in response.data


def test_get_books_route(client):
    """Test get books route."""
    with patch("app.get_books") as mock_get_books:
        mock_get_books.return_value = [
            Book(id=1, title="Test Book", author="Test Author")
        ]
        response = client.get("/books")

        assert response.status_code == 200
        assert b"Test Book" in response.data


def test_get_book_route(client):
    """Test get book route."""
    with patch("app.get_book") as mock_get_book:
        mock_get_book.return_value = Book(id=1, title="Test Book", author="Test Author")
        response = client.get("/books/1")

        assert response.status_code == 200
        assert b"Test Book" in response.data


def test_update_book_route(client):
    """Test update book route."""
    with patch("app.update_book") as mock_update_book:
        mock_update_book.return_value = Book(
            id=1, title="Updated Book", author="Test Author"
        )
        response = client.put(
            "/books/1", json={"title": "Updated Book", "author": "Test Author"}
        )

        assert response.status_code == 200
        assert b"Book updated successfully" in response.data


def test_delete_book_route(client):
    """Test delete book route."""
    with patch("app.delete_book") as mock_delete_book:
        mock_delete_book.return_value = True
        response = client.delete("/books/1")

        assert response.status_code == 200
        assert b"Book deleted successfully" in response.data


def test_search_books(client):
    """Test search books route."""
    with patch("app.search_books_by_title_or_author") as mock_search_books:
        mock_search_books.return_value = [
            Book(id=1, title="Test Book", author="Test Author")
        ]
        response = client.get("/search?search=Test")

        assert response.status_code == 200
        assert b"Test Book" in response.data

        assert b"Test Book" in response.data
