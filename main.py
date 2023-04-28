#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

DM = DataManager()
FS = FlightSearch()
NM = NotificationManager()

print('Welcome to the Flight Club.')
print('We find the best flight deals and email them to you.')
first_name = input('What is your first name?\n')
last_name = input('What is your last name?\n')
email = input('What is your email?\n')
email_confirmation = input('Type your email again.\n')

if email == email_confirmation:
    DM.add_user(first_name, last_name, email)

sheet_data = DM.get_flight_data()

for flight in sheet_data:
    if flight['iataCode'] == '':
        new_iata_code = FS.check_iata_code(flight)
        flight['iataCode'] = new_iata_code
        DM.update_flight_data(flight)
    else:
        flight_data = FS.flight_data_search(flight['iataCode'])
        if flight_data == None:
            continue
        if int(flight_data.price) < int(flight['lowestPrice']):
            users = DM.get_user_data()
            print(users)
            email_list = [row['email'] for row in users]

            content = (f"Low price alert! Only R${flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport} from {flight_data.out_date} to {flight_data.return_date}")
            if flight_data.stop_overs>0:
                content += (f"\nFlight has {flight_data.stop_overs}, via {flight_data.via_city }")

            NM.send_emails(email_list, content)