#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
import flight_search
import pprint
import datetime
from notification_manager import NotificationManager
DEPARTURECITYCODE="LON"


flight_searchObj=flight_search.FlightSearch()
data_managerObj=data_manager.DataManager()
sheetdata=data_managerObj.getSheetData()
for city in sheetdata:
    city["iataCode"]=flight_searchObj.codefinder(cityName=city["city"])

pprint.pprint(sheetdata)
#data_managerObj.updateSheet()

today=datetime.datetime.now()
tomorrow=today+datetime.timedelta(1)
sixmonth=today+datetime.timedelta(6*30)
print(tomorrow,sixmonth)

cheapflitfound=False
message=""
for city in sheetdata:
    flight=flight_searchObj.searchflight(DEPARTURECITYCODE,city["iataCode"],tomorrow,sixmonth)
    if flight!=None:
        print(flight.origin_city,flight.destination_city,flight.price,flight.stops,flight.via_city)
        if flight.price<city["lowestPrice"] and flight.stops==1:
            cheapflitfound = True
            message += f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}." \
                       f"\n Flight has one stop over, via {flight.via_city}\n\n"
        if flight.price<city["lowestPrice"]:
            cheapflitfound = True
            message+=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.\n\n"




sendsmsandmail=NotificationManager()
if cheapflitfound==True:
    print(message)

    sendsmsandmail.sendsmsalart(sms=message)


    custlist=data_managerObj.getcustomerdata()
    emaillist=[]
    for cust in custlist:
        emaillist.append(cust["email"])
    sendsmsandmail.sendemail(emaillist,message)
