from main import BooksCollector

import pytest


@pytest.mark.parametrize("book_name, genre", [["Туманность андромеды", "Фантастика"],
                                              ["Челюсти", "Ужасы"]])
def test_set_book_genre_add_two_books_and_genre(book_collector, book_name, genre):
    book_collector.add_new_book(book_name)
    book_collector.set_book_genre(book_name, genre)
    assert book_collector.books_genre[book_name] == genre


def test_add_new_book_add_two_books(book_collector):
    book_collector.add_new_book('Мама я тимлид')
    book_collector.add_new_book('Грокаем алгоритмы')
    assert len(book_collector.books_genre) == 2


@pytest.mark.parametrize("book_name, genre", [["Туманность андромеды", "Фантастика"],
                                              ["Челюсти", "Ужасы"]])
def test_get_book_genre_add_two_books_and_genre(book_collector, book_name, genre):
    book_collector.add_new_book(book_name)
    book_collector.set_book_genre(book_name, genre)
    assert book_collector.get_book_genre(book_name) == genre


def test_get_books_genre_add_one_book_and_genre(book_collector):
    book_collector.add_new_book("Властелин колец")
    book_collector.set_book_genre("Властелин колец", "Фантастика")
    assert book_collector.get_books_genre() == {"Властелин колец": "Фантастика"}


def test_get_books_for_children_add_two_books_with_genre(book_collector):
    book_collector.add_new_book("Волшебник изумрудного города")
    book_collector.set_book_genre("Волшебник изумрудного города", "Фантастика")
    book_collector.add_new_book("Молчание ягнят")
    book_collector.set_book_genre("Молчание ягнят", "Ужасы")
    assert book_collector.get_books_for_children() == ["Волшебник изумрудного города"]



def test_add_book_in_favorites_add_one_book(book_collector):
    book_collector.add_new_book("Ромео и Джульета")
    book_collector.add_book_in_favorites("Ромео и Джульета")
    assert "Ромео и Джульета" in book_collector.favorites


def test_delete_book_from_favorites_add_one_book_then_delete(book_collector):
    book_collector.add_new_book("Властелин колец")
    book_collector.add_book_in_favorites("Властелин колец")
    book_collector.delete_book_from_favorites("Властелин колец")
    assert "Властелин колец" not in book_collector.favorites


def test_get_list_of_favorites_books_add_one_book(book_collector):
    book_collector.add_new_book("Властелин колец")
    book_collector.add_book_in_favorites("Властелин колец")
    assert book_collector.get_list_of_favorites_books() == ["Властелин колец"]


def test_get_books_with_specific_genre_select_fantastic(book_collector):
    for name, genre in [["Туманность андромеды", "Фантастика"], ["Волшебник изумрудного города", "Фантастика"],
                        ['Челюсти', 'Ужасы'], ['Кто убил кролика Роджера', 'Детективы']]:
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
    assert (book_collector.get_books_with_specific_genre('Фантастика')) == ['Туманность андромеды',
                                                                            'Волшебник изумрудного города']
