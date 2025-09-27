import pytest

from main import BooksCollector


book_one = 'Гордость и предубеждение и зомби'
genre_one = 'Ужасы'
books_genre_one = {'Denny': 'Ужасы', '67': 'Комедии', 'Faust': 'Ужасы', 'Benny': 'Мультфильмы'}
#тестируем класс BooksCollector
class TestBooksCollector():

    #1.0 тестируем добавление книги и её повторное добавление
    def test_add_new_book_add_book(self, collector, add_one_book):
        collector.add_new_book(book_one)
        assert len(collector.books_genre) == 1

    #1.1 тестируем отсутствие жанра у добавленной книги
    def test_add_new_book_genre_is_empty(self, collector, add_one_book):
        assert collector.books_genre == {book_one: ''}

    #1.2 тестируем добавление при 0 и больше 40 символов
    @pytest.mark.parametrize('books',['', 'Что делать, если ваш кот хочет вас убить за десерт'])
    def test_add_new_book_books_not_add(self, collector, books):
        collector.add_new_book(books)
        assert len(collector.books_genre) == 0

    #2.0 тестируем добавление жанра книги, если книга есть в books_genre и её жанр входит в список genre
    def test_set_book_genre_add_genre(self, collector, add_one_book_genre):
        assert collector.books_genre == {book_one: genre_one}

    #2.1 тестируем добавление жанра книге, при невыполнении одного или нескольких условий
    #(книга есть в books_genre и её жанр входит в список genre)
    @pytest.mark.parametrize('book, genre',[[book_one, 'Триллер'],
                                            ['Санта', genre_one],
                                            ['Терминатор', 'Боевик']])
    def test_set_book_genre_genre_not_add(self, collector,add_one_book_genre, book, genre):
        collector.set_book_genre(book, genre)
        assert collector.books_genre == {book_one: genre_one}

    #3.0 тестируем вывод жанра книги по её имени
    def test_get_book_genre_get_genre(self, collector, add_one_book_genre):
        assert collector.get_book_genre(book_one) == genre_one

    #4.0 тестируем вывод списка книг с определённым жанром
    def test_get_books_with_specific_genre_get_list_books(self, collector):
        collector.books_genre = books_genre_one
        assert collector.get_books_with_specific_genre(genre_one) == ['Denny', 'Faust']
    
    #5.0 тестируем вывод текущего словаря books_genre
    def test_get_books_genre_get_dictionary_books_genre(self, collector):
        assert collector.get_books_genre() == {}

    #6.0 тестируем возврат книг, которые подходят детям
    def test_get_books_for_children_get_list_books_not_in_genre_age_rating(self,collector):
        collector.books_genre = books_genre_one
        assert collector.get_books_for_children() == ['67', 'Benny']

    #7.0 тестируем добавление книги в избранное и её повторное добавление
    def test_add_book_in_favorites_add_book(sels, collector, add_one_book_in_favorites):
        collector.add_book_in_favorites(book_one)
        assert len(collector.favorites) == 1

    #8.0 тестируем удаляение книги из избранного
    def test_delete_book_from_favorites_book_deleted(self, collector, add_one_book_in_favorites):
        collector.delete_book_from_favorites(book_one)
        assert collector.favorites == []

    #9.0 тестируем получение списка избранных книг
    def test_get_list_of_favorites_books_get_list_books(self, collector):
        assert collector.get_list_of_favorites_books() == []
