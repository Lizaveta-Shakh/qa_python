import pytest
from main import BooksCollector



@pytest.fixture (autouse=True)
def b_collection():
    return BooksCollector()


class TestBooksCollector:

    def test_add_new_book_add_two_books_add_books_in_books_genre(self, b_collection):

        b_collection.add_new_book('Гордость и предубеждение и зомби')
        b_collection.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(b_collection.get_books_genre()) == 2


def test_add_new_book_duplicate_does_not_add_again(b_collection):
    book_name = "Грозовой перевал"
    b_collection.add_new_book(book_name)
    assert book_name in b_collection.get_books_genre()

    b_collection.add_new_book(book_name)
    assert len(b_collection.get_books_genre()) == 1
    assert b_collection.get_books_genre()[book_name] == ''


@pytest.mark.parametrize ('book_name', ['A', 'AB', 'Человек-невидимка', 'Читать... Лев, колдунья и платяной шкаф', 'Общая теория занятости, процента и денег'])
def test_add_new_book_valid_lengths_add_books_in_books_genre(b_collection, book_name):
    b_collection.add_new_book(book_name)

    assert book_name in b_collection.get_books_genre()


@pytest.mark.parametrize("book_name, genre", [
    ("Гарри Поттер", "Фантастика"),
    ("Шерлок Холмс", "Детективы"),
    ("Король Лев", "Мультфильмы")
])
def test_set_book_genre_adds_valid_genre_to_existing_book(b_collection, book_name, genre):
    b_collection.add_new_book(book_name)
    b_collection.set_book_genre(book_name, genre)

    assert b_collection.get_book_genre(book_name) == genre



@pytest.mark.parametrize("book_name, genre", [
    ("Гарри Поттер", "Фантастика"),
    ("Шерлок Холмс", "Детективы"),
    ("Король Лев", "Мультфильмы"),
    ("Неизвестная книга", "")
])

def test_get_book_genre_returns_genre_for_book(b_collection, book_name, genre):
    b_collection.add_new_book(book_name)
    b_collection.set_book_genre(book_name, genre)

    assert b_collection.get_book_genre(book_name) == genre



@pytest.mark.parametrize("books, expected_books", [
    ({"Гарри Поттер": "Фантастика", "Дюна": "Фантастика", "Шерлок Холмс": "Детективы"},
     ["Гарри Поттер", "Дюна"]),

    ({"Гарри Поттер": "Фантастика"}, ["Гарри Поттер"]) ])

def test_get_books_with_specific_genre_fantasy_returns_fantasy_books_only(b_collection, books, expected_books):
    for book, book_genre in books.items():
        b_collection.add_new_book(book)
        b_collection.set_book_genre(book, book_genre)

    assert sorted(b_collection.get_books_with_specific_genre("Фантастика")) == sorted(expected_books)



@pytest.mark.parametrize("books, expected_books", [
    ({"Гарри Поттер": ""}, {"Гарри Поттер": ""}),
    ({"Гарри Поттер": "Фантастика", "Дюна": "Фантастика"},
     {"Гарри Поттер": "Фантастика", "Дюна": "Фантастика"}),
    ({}, {})
    ])

def test_get_books_genre_returns_books_genre_dict(b_collection, books, expected_books):

    for book, book_genre in books.items():
        b_collection.add_new_book(book)
        if book_genre:
            b_collection.set_book_genre(book, book_genre)

    assert b_collection.get_books_genre() == expected_books



@pytest.mark.parametrize("books, expected_books", [
    ({"Гарри Поттер": "Фантастика", "Дюна": "Фантастика", "Шерлок Холмс": "Детективы", "Оно": "Ужасы"},
     ["Гарри Поттер", "Дюна"]),
    ({"Гарри Поттер": "Фантастика", "Чип и Дейл": "Мультфильмы"},
     ["Гарри Поттер", "Чип и Дейл"])
])
def test_get_books_for_children_returns_books_without_age_raiting(b_collection, books, expected_books):
    for book, genre in books.items():
        b_collection.add_new_book(book)
        b_collection.set_book_genre(book, genre)

    result = b_collection.get_books_for_children()

    for book in result:
        genre = b_collection.get_book_genre(book)
        assert genre not in b_collection.genre_age_rating




def test_add_book_in_favorites_one_book_adds_in_favorites(b_collection):
    book_name = "Повелитель мух"
    b_collection.add_new_book(book_name)
    b_collection.add_book_in_favorites(book_name)

    assert book_name in b_collection.favorites



def test_delete_book_from_favorites_one_book_deletes_from_favorites (b_collection):
    book_name = "Повелитель мух"
    b_collection.add_new_book(book_name)
    b_collection.add_book_in_favorites(book_name)

    b_collection.delete_book_from_favorites(book_name)

    assert book_name not in b_collection.get_list_of_favorites_books()



@pytest.mark.parametrize("books", [
        (["Гарри Поттер", "Дюна"]),
        (["Мастер и Маргарита", "1984"])
    ])
def test_get_list_of_favorites_books_returns_favorites_list (b_collection, books):

    for book in books:
        b_collection.add_new_book(book)
        b_collection.add_book_in_favorites(book)

    assert b_collection.get_list_of_favorites_books() == books
