from model import AirportModel
from view import AirportView
import tkinter as tk
from tkinter import simpledialog, messagebox
import mysql.connector

class AirportController:
    """
    Контроллер для взаимодействия между моделью и представлением.
    """
    def __init__(self, model, view):
        """
        Инициализация контроллера с моделью и представлением.

        :param model: Экземпляр модели AirportModel.
        :param view: Экземпляр представления AirportView.
        """
        self.model = model
        self.view = view
        self.view.filter_button_clicked_callback = self.filter_airports
        self.view.search_flights_button_clicked_callback = self.search_flights
        self.view.search_flights_from_city_button_clicked_callback = self.search_flights_from_city

    def filter_airports(self):
        """
        Обработка события фильтрации аэропортов.
        """
        try:
            min_lat = float(self.view.min_lat_entry.get())
            max_lat = float(self.view.max_lat_entry.get())
            min_lon = float(self.view.min_lon_entry.get())
            max_lon = float(self.view.max_lon_entry.get())
            filtered_data = self.model.filter_airports(min_lat, max_lat, min_lon, max_lon)
            self.view.update_table(filtered_data)
        except ValueError:
            pass

    def search_flights(self):
        """
        Обработка события поиска рейсов между двумя городами.
        """
        try:
            source_city = self.view.source_city_entry.get()
            dest_city = self.view.dest_city_entry.get()
            flights_data = self.model.get_flights_between_cities(source_city, dest_city)
            self.view.update_flights_table(flights_data)
        except ValueError:
            pass

    def search_flights_from_city(self):
        """
        Обработка события поиска рейсов из указанного города.
        """
        try:
            city = self.view.city_entry.get()
            flights_data = self.model.get_flights_from_city(city)
            self.view.update_flights_table(flights_data)
        except ValueError:
            pass

    def close(self):
        """
        Закрытие соединения с базой данных.
        """
        self.model.close()

def get_db_config():
    """
    Получение конфигурации базы данных от пользователя.

    :return: Словарь с параметрами подключения к базе данных.
    """
    root = tk.Tk()
    root.withdraw()  # Скрытие основного окна

    user = simpledialog.askstring("Input", "Enter MySQL username:", parent=root)
    password = simpledialog.askstring("Input", "Enter MySQL password:", parent=root, show='*')

    return {
        'user': user,
        'password': password,
        'host': '127.0.0.1',
        'database': 'flights',
        'port': 3306
    }

def create_model(db_config):
    """
    Создание модели с обработкой ошибок подключения.

    :param db_config: Словарь с параметрами подключения к базе данных.
    :return: Экземпляр модели AirportModel или None в случае ошибки.
    """
    try:
        return AirportModel(db_config)
    except mysql.connector.Error as err:
        messagebox.showerror("Database Connection Error", f"Error: {err}")
        return None

if __name__ == "__main__":
    # Получение конфигурации базы данных от пользователя
    db_config = get_db_config()

    # Создание экземпляров модели, представления и контроллера
    root = tk.Tk()
    model = create_model(db_config)
    if model:
        view = AirportView(root)
        controller = AirportController(model, view)
        root.mainloop()
        controller.close()
    else:
        root.destroy()  # Закрытие основного окна в случае ошибки подключения
