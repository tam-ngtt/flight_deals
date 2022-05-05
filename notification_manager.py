from twilio.rest import Client
import os

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        account_sid = "AC863b434a4a3d3738e5cc091b474c9967"
        auth_token = "c20130636b877806c9758f1f2bffe44e"
        self.PHONE_NUMBER = "+17652751164"
        self.client = Client(account_sid, auth_token)

    def send_message(self, flight_info):
        message = self.client.messages \
            .create(
                body=f"Low price alert! Only {flight_info['price']} {flight_info['currency']} to fly "
                     f"from {flight_info['dep_city']}-{flight_info['dep_airport']} "
                     f"to {flight_info['des_city']}-{flight_info['des_airport']}, "
                     f"from {flight_info['inbound']} to {flight_info['outbound']}.",
                from_=self.PHONE_NUMBER,
                to=os.environ.get("MY_PHONE"))
        print(message.status)
        #
        # print(f"Low price alert! Only {flight_info['price']} {flight_info['currency']} to fly "
        #       f"from {flight_info['dep_city']}-{flight_info['dep_airport']} "
        #       f"to {flight_info['des_city']}-{flight_info['des_airport']}, "
        #       f"from {flight_info['inbound']} to {flight_info['outbound']}.")
