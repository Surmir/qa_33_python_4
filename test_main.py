import pytest

from main import BooksCollector


book_one = 'Гордость и предубеждение и зомби'
genre_one = 'Ужасы'
books_genre_one = {'Denny': 'Ужасы', '67': 'Комедии', 'Faust': 'Ужасы', 'Benny': 'Мультфильмы'}
books_favorites_one = ['Denny', '67', 'Faust', 'Benny']

#тестируем класс BooksCollector
class TestBooksCollector():

    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()
        return self.collector

    #1.0 добавление книги и её повторное добавление
    def test_add_new_book_add_book(self):
        self.collector.add_new_book(book_one)
        self.collector.add_new_book(book_one)
        assert len(self.collector.books_genre) == 1

    #1.1 отсутствие жанра у добавленной книги
    def test_add_new_book_genre_is_empty(self):
        self.collector.add_new_book(book_one)
        assert self.collector.books_genre == {book_one: ''}

    #1.2 добавление при 0 и больше 40 символов
    @pytest.mark.parametrize('books',['', 'Ч' * 41])
    def test_add_new_book_books_not_add(self, books):
        self.collector.add_new_book(books)
        assert len(self.collector.books_genre) == 0

    #2.0 добавление жанра книги, если книга есть в books_genre и её жанр входит в список genre
    def test_set_book_genre_add_genre(self):
        self.collector.books_genre = {book_one: ''}
        self.collector.set_book_genre(book_one, genre_one)
        assert self.collector.books_genre == {book_one: genre_one}

    #2.1 добавление жанра книге, при отсутствие жанра в genre
    def test_set_book_genre_genre_not_add(self):
        self.collector.books_genre = {book_one: ''}
        self.collector.set_book_genre(book_one, 'Триллер')
        assert self.collector.books_genre == {book_one: ''}

    #3.0 вывод жанра книги по её имени
    def test_get_book_genre_get_genre(self):
        self.collector.books_genre = {book_one: genre_one}
        assert self.collector.get_book_genre(book_one) == genre_one

    #4.0 вывод списка книг с определённым жанром
    def test_get_books_with_specific_genre_get_list_books(self):
        self.collector.books_genre = books_genre_one
        assert self.collector.get_books_with_specific_genre(genre_one) == ['Denny', 'Faust']
    
    #5.0 вывод текущего словаря books_genre
    def test_get_books_genre_get_dictionary_books_genre(self):
        self.collector.books_genre = books_genre_one
        assert self.collector.get_books_genre() == books_genre_one

    #6.0 возврат книг, которые подходят детям
    def test_get_books_for_children_get_list_books_not_in_genre_age_rating(self):
        self.collector.books_genre = books_genre_one
        assert self.collector.get_books_for_children() == ['67', 'Benny']

    #7.0 добавление книги в избранное и её повторное добавление
    def test_add_book_in_favorites_add_book(self):
        self.collector.books_genre = {book_one: genre_one}
        self.collector.add_book_in_favorites(book_one)
        self.collector.add_book_in_favorites(book_one)
        assert len(self.collector.favorites) == 1

    #8.0 удаляение книги из избранного
    def test_delete_book_from_favorites_book_deleted(self):
        self.collector.favorites = [book_one]
        self.collector.delete_book_from_favorites(book_one)
        assert self.collector.favorites == []

    #9.0 получение списка избранных книг
    def test_get_list_of_favorites_books_get_list_books(self):
        self.collector.favorites = books_favorites_one
        assert self.collector.get_list_of_favorites_books() == books_favorites_one
