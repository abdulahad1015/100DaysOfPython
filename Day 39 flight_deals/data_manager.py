import requests
from pprint import pprint


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_URL = "https://api.sheety.co/25865526c7240d7293b60bb2829ae102/flightDeals/prices"
        self.SHEETY_HEADER = {
            "Content-Type": "application/json"
        }

    def Get_IATA(self):
        response = requests.get(url=self.SHEETY_URL)
        sheet_data = response.json()['prices']
        for i in sheet_data:
            i['iataCode'] = "a"
            row={
                'price':i
            }
            sheety_url=f"{self.SHEETY_URL}/{i['id']}"
            # print(url)
            # print(row)
            # response = requests.put(url=sheety_url, json=row)
            # print(response.text)
            # break

        pprint(sheet_data)
        print(response)


a = DataManager()
a.Get_IATA()
