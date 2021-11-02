import sqlite3

from sqlite_to_postgres.dataclases import FilmWork, Genre, Person


class SQLiteLoader:
    """ Класс получения данных из базы SqlLite """

    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def get_all_movies(self) -> list:
        """ Получение всех фильмов из базы """

        movies = []
        query = """SELECT * FROM film_work"""
        for movie in self.cursor.execute(query):
            film_work = FilmWork(title=movie['title'],
                                 description=movie['description'],
                                 creation_date=movie['creation_date'],
                                 certificate=movie['certificate'], file_path=movie['file_path'],
                                 rating=movie['rating'], type=movie['type'], created_at=movie['created_at'],
                                 updated_at=movie['updated_at'],
                                 id=movie['id'])
            movies.append(film_work)
        return movies

    def get_all_genres(self) -> list:
        """ Получение всех жанров из базы """

        genres = []
        query = """SELECT * FROM genre"""
        for genre in self.cursor.execute(query):
            genres.append(Genre(
                id=genre["id"], name=genre["name"], description=genre["description"],
                created_at=genre["created_at"], updated_at=genre["updated_at"]
            ))
        return genres

    def get_all_persons(self) -> list:
        """ Получение всех персон из таблицы person """

        persons = []
        query = """SELECT * FROM person"""
        for person in self.cursor.execute(query):
            persons.append(Person(id=person["id"], full_name=person["full_name"], birth_date=person["birth_date"],
                                  created_at=person["created_at"], updated_at=person["updated_at"]
                                  ))
        return persons

    def load_movies(self) -> dict:
        """ Возвращает словарь с данными из таблиц person, film_work, genre """

        return {
            "film_work": self.get_all_movies(),
            "genre": self.get_all_genres(),
            "person": self.get_all_persons()
        }
