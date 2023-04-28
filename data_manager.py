import os
from dotenv import load_dotenv
import requests
load_dotenv()

SHEETY_API_KEY = os.environ.get('SHEETY_API_KEY')
SHEETY_AUTH = os.environ.get('SHEETY_AUTH')
SHEETY_APP_ID = os.environ.get('SHEETY_APP_ID')
SHEETY_PRICES_ENDPOINT = os.environ.get('SHEETY_PRICES_ENDPOINT')
SHEETY_USERS_ENDPOINT = os.environ.get('SHEETY_USERS_ENDPOINT')


sheety_headers = {
    'x-app-id': SHEETY_APP_ID,
    'x-app-key': SHEETY_API_KEY,
    'Authorization': SHEETY_AUTH
    }

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def get_flight_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,headers=sheety_headers)
        sheet_data = response.json()['prices']
        return sheet_data
    
    def update_flight_data(self,flight):
        flight_params = {
        'price':{
        'city':flight['city'],
        'iataCode':flight['iataCode'],
        'lowestPrice':flight['lowestPrice'],
        }
    }
        response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{flight['id']}", json=flight_params, headers=sheety_headers)
        print(response.text)

    def add_user(self, first_name, last_name, email):
        user_params = {
            'user':{
                'firstName':first_name,
                'lastName':last_name,
                'email':email
            }
        }
        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=user_params, headers=sheety_headers)
        if response.status_code == '200':
            print('Your email has been added, welcome to the Flight Club!')
    
    def get_user_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=sheety_headers)
        self.user_data = response.json()['users']
        return self.user_data
