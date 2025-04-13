import requests
from twilio.rest import Client

MY_lat = os.gitenv("LAT")
My_long = os.gitenv("LON")

account_sid = os.gitenv("TWILIO_SID")
auth_token = os.gitenv("TWILIO_AUTH_TOKEN")

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key = os.gitenv("OWM_API_KEY")

parameters = {
    "lon": My_long,
    "lat": MY_lat,
    "appid":api_key,
    "cnt":4
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
whether_data = response.json()

will_rain = False
for hour_data in whether_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=os.gitenv("FROM_WHATSAPP"),
        body="It's going to rain today. Remember to bring an ☂️",
        to=os.gitenv("TO_WHATSAPP")
    )

    print(message.status)