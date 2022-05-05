import requests
from data_manager import DataManager
import datetime

FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
API_KEY = "2afQ7nTqtKgIkKCEh2k_EhkIjmU8X5qr"
HEADERS = {
    "apikey": API_KEY,
    "Content-Encoding": "gzip"
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city_data: DataManager):
        self.city_names = city_data.city_name_list
        self.city_code = city_data.city_info
        self.flights_found = {}
        self.flight_response()

    def flight_response(self):
        start_date = datetime.date.today() + datetime.timedelta(days=1)
        end_date = datetime.date.today() + datetime.timedelta(days=6*30)
        for city in self.city_names:
            flight_params = {
                "fly_from": "LON",
                "fly_to": self.city_code[city]["ct_code"],
                "date_from": start_date,
                "date_to": end_date,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "curr": "GBP",
                "max_stopovers": 0,
            }
            response = requests.get(url=FLIGHT_ENDPOINT, params=flight_params, headers=HEADERS)
            data = response.json()["data"]
            self.flights_found[city] = data
