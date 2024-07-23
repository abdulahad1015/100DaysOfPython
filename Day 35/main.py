import requests
from twilio.rest import Client
#25UNEMW7J9X7U6RQ2XZATLF3

OWM_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
api_key="f7130eaf3ad5d762f4100d5f9acb337a"



parameters={
    "lat":24.55,
    "lon":67.033,
    "appid":api_key,
    "cnt":4,
    "units":"metric"
}

response=requests.get(OWM_ENDPOINT,params=parameters)
response.raise_for_status()
data=response.json()

rain=False
for i in data["list"]:
    condition_codes=i["weather"][0]["id"]
    if(int(condition_codes)<700):
        rain=True

if rain:
    print("Bring an Umbrella")
    client =  Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    # message=client.messages.create(body="It's going to rain",from_='+18669356050',to='+14046696896')
    # print(message.status)