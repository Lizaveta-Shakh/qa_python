Для удобства работы с тестами, была создана фикстура для создания новых экземпляров класса BooksCollector для каждого теста. Фикстура не выносилась в отдельный файл и указана прямо в тестовом файле.


1. test_add_new_book_add_two_books_add_books_in_books_genre - проверяет корректное добавление 2х книг в словарь books_genre.

2. test_add_new_book_duplicate_does_not_add_again - проверяет, что добавление одной и той же книги несколько раз не приводит к появлению дубликатов в словаре books_genre.

3. test_add_new_book_valid_lengths_add_books_in_books_genre - проверяет успешное добавление в словарь books_genre книг с длинной названия, соответствующей требованиям(1,2,17,39,40 символов). Использована параметризация.

4. test_set_book_genre_adds_valid_genre_to_existing_book  - проверяет корректное добавление жанра книги из списка genre к книге из books_genre.

5. test_get_book_genre_returns_genre_for_book - проверяет вывод  жанра книги, который соответствует ее названию в словаре books_genre.

6. test_get_books_with_specific_genre_fantasy_returns_fantasy_books_only - проверка корректного определения и вывода книг с жанром "Фантастика".

7. test_get_books_genre_returns_books_genre_dict - проверка корректного вывода актуального словаря books_genre.

8. test_get_books_for_children_returns_books_without_age_raiting - корректная выборка и вывод названий книг из books_genre, которые не входят в список genre_age_rating.

9. test_add_book_in_favorites_one_book_adds_in_favorites - проверяет корректное добавление книги в список favorites.


10. test_delete_book_from_favorites_one_book_deletes_from_favorites
Проверка успешного удаления книги из списка favorites.

11. test_get_list_of_favorites_books_returns_favorites_list - проверка вывода актуального списка книг из списка favorites.



# qa_python
