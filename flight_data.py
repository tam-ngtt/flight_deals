from flight_search import FlightSearch
from data_manager import DataManager


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flights_data: FlightSearch, city_data: DataManager):
        self.raw_data = flights_data.flights_found
        self.city_names = city_data.city_name_list
        self.city_info = city_data.city_info
        self.total_flights_data = {}

        for city in self.city_names:
            current_city = self.raw_data[city]
            flight_formatted_data = [{"dep_airport": current_city[i]["flyFrom"],
                                      "des_airport": current_city[i]["flyTo"],
                                      "price": current_city[i]["price"],
                                      "currency": list(current_city[i]['conversion'].keys())[0],
                                      "duration": current_city[i]["nightsInDest"],
                                      "inbound": current_city[i]["route"][0]["local_departure"].split("T")[0],
                                      "outbound":current_city[i]["route"][1]["local_departure"].split("T")[0],
                                      "dep_city": current_city[i]["cityFrom"],
                                      "des_city": current_city[i]["cityTo"]} for i in range(len(current_city))]
            self.total_flights_data[city] = flight_formatted_data

