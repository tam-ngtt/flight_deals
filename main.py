# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData
import datetime
import requests

city_data = DataManager()

flights = FlightSearch(city_data)

notification = NotificationManager()

flight_data = FlightData(city_data=city_data, flights_data=flights)


for city in city_data.city_name_list:
    lowest_price = city_data.city_info[city]["lowest_price"]
    for flight in flight_data.total_flights_data[city]:
        if flight["price"] < lowest_price:
            notification.send_message(flight)

