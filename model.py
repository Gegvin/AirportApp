import mysql.connector


class AirportModel:
    """
    Модель для взаимодействия с базой данных аэропортов и рейсов.
    """

    def __init__(self, db_config):
        """
        Инициализация модели с конфигурацией базы данных.

        :param db_config: Словарь с параметрами подключения к базе данных.
        """
        self.connection = mysql.connector.connect(
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            database=db_config['database'],
            port=db_config['port']
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def filter_airports(self, min_lat, max_lat, min_lon, max_lon):
        """
        Фильтрация аэропортов по заданным координатам.

        :param min_lat: Минимальная широта.
        :param max_lat: Максимальная широта.
        :param min_lon: Минимальная долгота.
        :param max_lon: Максимальная долгота.
        :return: Список аэропортов, удовлетворяющих условиям фильтрации.
        """
        query = """
        SELECT city, country, latitude, longitude
        FROM airports
        WHERE latitude BETWEEN %s AND %s
        AND longitude BETWEEN %s AND %s
        """
        self.cursor.execute(query, (min_lat, max_lat, min_lon, max_lon))
        result = self.cursor.fetchall()
        return result

    def get_flights_between_cities(self, source_city, dest_city):
        """
        Получение рейсов между двумя городами.

        :param source_city: Город отправления.
        :param dest_city: Город назначения.
        :return: Список рейсов между указанными городами.
        """
        query = """
        SELECT r.airline, r.src_airport, a1.city AS source_city, a1.country AS source_country,
               a1.airport AS source_airport, r.dst_airport, a2.city AS dest_city,
               a2.country AS dest_country, a2.airport AS dest_airport
        FROM routes r
        JOIN airports a1 ON r.src_airport = a1.iata
        JOIN airports a2 ON r.dst_airport = a2.iata
        WHERE a1.city = %s AND a2.city = %s
        """
        self.cursor.execute(query, (source_city, dest_city))
        result = self.cursor.fetchall()
        return result

    def get_flights_from_city(self, city):
        """
        Получение всех рейсов из указанного города.

        :param city: Город отправления.
        :return: Список рейсов из указанного города.
        """
        query = """
        SELECT r.airline, r.src_airport, a1.city AS source_city, a1.country AS source_country,
               a1.airport AS source_airport, r.dst_airport, a2.city AS dest_city,
               a2.country AS dest_country, a2.airport AS dest_airport
        FROM routes r
        JOIN airports a1 ON r.src_airport = a1.iata
        JOIN airports a2 ON r.dst_airport = a2.iata
        WHERE a1.city = %s
        """
        self.cursor.execute(query, (city,))
        result = self.cursor.fetchall()
        return result

    def close(self):
        """
        Закрытие соединения с базой данных.
        """
        self.cursor.close()
        self.connection.close()
