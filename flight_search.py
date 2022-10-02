import requests

from flight_data import FlightData

TEQUILA_END_POINT="https://tequila-api.kiwi.com/locations/query"
TEQUILA_SEARCH_END_POINT="https://tequila-api.kiwi.com/v2/search"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.


    def codefinder(self,cityName:str):
        destheader={
            "apikey": "M2HbhhachLkGt2p6scKy3kDsTiRWxPQp",
        }
        destdata={
            "term":cityName
        }

        response=requests.get(TEQUILA_END_POINT,params=destdata,headers=destheader)
        response.raise_for_status()
        outdata=response.json()
        code=outdata["locations"][0]["code"]
        return code



    def searchflight(self,origin_city_code,destination_city_code,from_time,to_time):
        fliteheader={
            "apikey": "M2HbhhachLkGt2p6scKy3kDsTiRWxPQp",
        }
        searchparam={
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        flitesearchresponse=requests.get(url=TEQUILA_SEARCH_END_POINT,params=searchparam,headers=fliteheader)
        flitesearchresponse.raise_for_status()
        try:
            flitesearchresponseData=flitesearchresponse.json()["data"][0]
        except IndexError:
            searchparam["max_stopovers"]=1
            try:
                flitesearchresponse = requests.get(url=TEQUILA_SEARCH_END_POINT, params=searchparam, headers=fliteheader)
                flitesearchresponseData = flitesearchresponse.json()["data"][0]
                print("no direct filight found for ",origin_city_code,destination_city_code)
                flight = FlightData(price=flitesearchresponseData["price"],
                                    origin_city=flitesearchresponseData["route"][0]["cityFrom"],
                                    destination_city=flitesearchresponseData["route"][1]["cityTo"],
                                    origin_airport=flitesearchresponseData["route"][0]["flyFrom"],
                                    destination_airport=flitesearchresponseData["route"][1]["flyTo"],
                                    out_date=flitesearchresponseData["route"][0]["local_departure"].split("T")[0],
                                    return_date=flitesearchresponseData["route"][1]["local_arrival"].split("T")[0],
                                    stops=1,
                                    via_city=flitesearchresponseData["route"][0]["cityTo"])
            except IndexError:
                print("no 1 stop filight found for ", origin_city_code, destination_city_code)
                return None
        else:
            flight=FlightData(price=flitesearchresponseData["price"],
                              origin_city=flitesearchresponseData["route"][0]["cityFrom"],
                              destination_city=flitesearchresponseData["route"][0]["cityTo"],
                              origin_airport=flitesearchresponseData["route"][0]["flyFrom"],
                              destination_airport=flitesearchresponseData["route"][0]["flyTo"],
                              out_date=flitesearchresponseData["route"][0]["local_departure"].split("T")[0],
                              return_date=flitesearchresponseData["route"][0]["local_arrival"].split("T")[0],
        )
        return flight