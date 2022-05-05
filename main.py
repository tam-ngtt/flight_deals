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


# FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
# API_KEY = "2afQ7nTqtKgIkKCEh2k_EhkIjmU8X5qr"
# HEADERS = {
#     "apikey": API_KEY,
#     "Content-Encoding": "gzip"
# }
#
# start_date = datetime.date.today() + datetime.timedelta(days=1)
# end_date = datetime.date.today() + datetime.timedelta(days=6 * 30)
# for city in city_data.city_name_list:
#     flight_params = {
#         "fly_from": "LON",
#         "fly_to": city_data.city_info[city]["ct_code"],
#         "date_from": start_date,
#         "date_to": end_date,
#         "nights_in_dst_from": 7,
#         "nights_in_dst_to": 28,
#         "flight_type": "round",
#         "one_for_city": 1,
#         "curr": "GBP",
#         "max_stopovers": 0,
#     }
#     response = requests.get(url=FLIGHT_ENDPOINT, params=flight_params, headers=HEADERS)
#     data = response.json()
#     print(data)