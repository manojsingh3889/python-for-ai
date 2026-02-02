import requests



def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    
    response = requests.get(url)
    data  = response.json()
    temp = data["current"]["temperature_2m"]
    print(f"weather here is {temp}")
    pass

get_weather(34.4,56.5)

