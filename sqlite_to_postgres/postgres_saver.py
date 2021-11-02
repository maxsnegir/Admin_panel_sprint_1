from sqlite_to_postgres.dataclases import FilmWork, Genre, Person
from dataclasses import astuple


class PostgresSaver:
    """ Класс для загрузки данных в postgres """

    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def save_all_data(self, data: dict) -> bool:
        """ Основной метод для загрузки данных в таблицы postgres """

        slots = {
            "film_work": tuple(FilmWork.__slots__),
            "genre": tuple(Genre.__slots__),
            "person": tuple(Person.__slots__)
        }

        for table, values in data.items():

            # Определяем сколько значений нужно вставить в таблицу
            values_count = ", ".join(["%s" for _ in range(len(slots.get(table)))])
            args = ', '.join(self.cursor.mogrify(f"({values_count})", astuple(row)).decode() for row in values)

            query = """INSERT INTO content.{}  VALUES {} ON CONFLICT (id) DO NOTHING""".format(table, args)
            self.cursor.execute(query)
        return True





