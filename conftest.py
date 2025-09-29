import pytest
from main import BooksCollector


book_one = 'Гордость и предубеждение и зомби'
genre_one = 'Ужасы'

#класс BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

#есть книга в словаре
@pytest.fixture
def book_in_dictionaries(collector):
    collector.books_genre = {book_one: ''}

#есть книга с жанром в словаре
@pytest.fixture
def book_with_genre_in_dictionaries(collector):
    collector.books_genre = {book_one: genre_one}

#есть книга в избранном
@pytest.fixture
def book_in_favorites(collector):
    collector.favorites = [book_one]
