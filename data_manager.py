import  requests
import pprint

SHEETY_END_POINT = "https://api.sheety.co/cd5f060b0aed801a1de16665b1b72f57/flightDeals/prices"
SHEETY_CUS_API="https://api.sheety.co/cd5f060b0aed801a1de16665b1b72f57/flightDeals/customer"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __int__(self):
        GoogleSheetData={}
    def getSheetData(self):
        response=requests.get(url=SHEETY_END_POINT)
        #responseJson = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}
        responseJson =response.json()
        response.raise_for_status()

        self.GoogleSheetData=responseJson['prices']
        return self.GoogleSheetData

    def updateSheet(self):
        for city in self.GoogleSheetData:
            newdata={
                "price":{
                    "iataCode":city["iataCode"]
                }

            }

            response =requests.put(url=f"{SHEETY_END_POINT}/{city['id']}", json=newdata)
            print(self.GoogleSheetData[1]['id'])
            print(response)

    def getcustomerdata(self):
        custdata=requests.get(url=SHEETY_CUS_API).json()
        return custdata["customer"]

