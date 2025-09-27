import pytest
from main import BooksCollector



book_one = 'Гордость и предубеждение и зомби'
genre_one = 'Ужасы'

#класс BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

#добавляем книгу 'Гордость и предубеждение и зомби'
@pytest.fixture
def add_one_book(collector):
    add_one_book = collector.add_new_book(book_one)
    return add_one_book

#добавляем жанр книге 'Гордость и предубеждение и зомби'
@pytest.fixture
def add_one_book_genre(collector, add_one_book):
    add_one_book_genre = collector.set_book_genre(book_one, genre_one)
    return add_one_book_genre

#добавляем книгу в избранное
@pytest.fixture
def add_one_book_in_favorites(collector, add_one_book_genre):
    add_one_book_in_favorites = collector.add_book_in_favorites(book_one)
    return add_one_book_in_favorites
