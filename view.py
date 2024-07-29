import tkinter as tk
from tkinter import ttk

class AirportView:
    """
    Представление для отображения фильтрации аэропортов и поиска рейсов.
    """
    def __init__(self, root):
        """
        Инициализация представления.

        :param root: Корневое окно Tkinter.
        """
        self.root = root
        self.root.title("Airport Filter")

        self.create_widgets()

    def create_widgets(self):
        """
        Создание виджетов интерфейса.
        """
        # Создание рамки для фильтрации аэропортов
        filter_frame = tk.Frame(self.root)
        filter_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.min_lat_label = tk.Label(filter_frame, text="Min Latitude:")
        self.min_lat_label.grid(row=0, column=0, sticky=tk.W)
        self.min_lat_entry = tk.Entry(filter_frame)
        self.min_lat_entry.grid(row=0, column=1)

        self.max_lat_label = tk.Label(filter_frame, text="Max Latitude:")
        self.max_lat_label.grid(row=0, column=2, sticky=tk.W)
        self.max_lat_entry = tk.Entry(filter_frame)
        self.max_lat_entry.grid(row=0, column=3)

        self.min_lon_label = tk.Label(filter_frame, text="Min Longitude:")
        self.min_lon_label.grid(row=1, column=0, sticky=tk.W)
        self.min_lon_entry = tk.Entry(filter_frame)
        self.min_lon_entry.grid(row=1, column=1)

        self.max_lon_label = tk.Label(filter_frame, text="Max Longitude:")
        self.max_lon_label.grid(row=1, column=2, sticky=tk.W)
        self.max_lon_entry = tk.Entry(filter_frame)
        self.max_lon_entry.grid(row=1, column=3)

        self.filter_button = tk.Button(filter_frame, text="Filter", command=self.filter_button_clicked)
        self.filter_button.grid(row=2, column=0, columnspan=4, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("city", "country", "latitude", "longitude"), show="headings")
        self.tree.heading("city", text="City")
        self.tree.heading("country", text="Country")
        self.tree.heading("latitude", text="Latitude")
        self.tree.heading("longitude", text="Longitude")
        self.tree.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

        # Создание рамки для поиска рейсов
        flights_frame = tk.Frame(self.root)
        flights_frame.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.source_city_label = tk.Label(flights_frame, text="Source City:")
        self.source_city_label.grid(row=0, column=0, sticky=tk.W)
        self.source_city_entry = tk.Entry(flights_frame)
        self.source_city_entry.grid(row=0, column=1)

        self.dest_city_label = tk.Label(flights_frame, text="Destination City:")
        self.dest_city_label.grid(row=0, column=2, sticky=tk.W)
        self.dest_city_entry = tk.Entry(flights_frame)
        self.dest_city_entry.grid(row=0, column=3)

        self.search_flights_button = tk.Button(flights_frame, text="Search Flights", command=self.search_flights_button_clicked)
        self.search_flights_button.grid(row=1, column=0, columnspan=4, pady=10)

        self.city_label = tk.Label(flights_frame, text="City:")
        self.city_label.grid(row=2, column=0, sticky=tk.W)
        self.city_entry = tk.Entry(flights_frame)
        self.city_entry.grid(row=2, column=1)

        self.search_flights_from_city_button = tk.Button(flights_frame, text="Search Flights From City", command=self.search_flights_from_city_button_clicked)
        self.search_flights_from_city_button.grid(row=2, column=2, columnspan=2, pady=10)

        self.flights_tree = ttk.Treeview(self.root, columns=("airline", "src_airport", "source_city", "source_country", "source_airport", "dst_airport", "dest_city", "dest_country", "dest_airport"), show="headings")
        self.flights_tree.heading("airline", text="Airline")
        self.flights_tree.heading("src_airport", text="Source Airport")
        self.flights_tree.heading("source_city", text="Source City")
        self.flights_tree.heading("source_country", text="Source Country")
        self.flights_tree.heading("source_airport", text="Source Airport")
        self.flights_tree.heading("dst_airport", text="Destination Airport")
        self.flights_tree.heading("dest_city", text="Destination City")
        self.flights_tree.heading("dest_country", text="Destination Country")
        self.flights_tree.heading("dest_airport", text="Destination Airport")
        self.flights_tree.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

        # Установка ширины столбцов
        self.flights_tree.column("airline", width=50)
        self.flights_tree.column("src_airport", width=100)
        self.flights_tree.column("source_city", width=100)
        self.flights_tree.column("source_country", width=100)
        self.flights_tree.column("source_airport", width=150)
        self.flights_tree.column("dst_airport", width=120)
        self.flights_tree.column("dest_city", width=100)
        self.flights_tree.column("dest_country", width=120)
        self.flights_tree.column("dest_airport", width=150)

    def filter_button_clicked(self):
        """
        Обработка нажатия кнопки фильтрации аэропортов.
        """
        if hasattr(self, 'filter_button_clicked_callback'):
            self.filter_button_clicked_callback()

    def search_flights_button_clicked(self):
        """
        Обработка нажатия кнопки поиска рейсов между двумя городами.
        """
        if hasattr(self, 'search_flights_button_clicked_callback'):
            self.search_flights_button_clicked_callback()

    def search_flights_from_city_button_clicked(self):
        """
        Обработка нажатия кнопки поиска рейсов из указанного города.
        """
        if hasattr(self, 'search_flights_from_city_button_clicked_callback'):
            self.search_flights_from_city_button_clicked_callback()

    def update_table(self, data):
        """
        Обновление таблицы аэропортов.

        :param data: Список аэропортов для отображения.
        """
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in data:
            self.tree.insert("", "end", values=(row['city'], row['country'], row['latitude'], row['longitude']))

    def update_flights_table(self, data):
        """
        Обновление таблицы рейсов.

        :param data: Список рейсов для отображения.
        """
        for row in self.flights_tree.get_children():
            self.flights_tree.delete(row)
        for row in data:
            self.flights_tree.insert("", "end", values=(row['airline'], row['src_airport'], row['source_city'],
                                                        row['source_country'], row['source_airport'], row['dst_airport'],
                                                        row['dest_city'], row['dest_country'], row['dest_airport']))
