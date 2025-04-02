from flask import Flask
from dotenv import load_dotenv
import requests
import os

load_dotenv() 

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")  
CITIES = [
    "Kyiv", "Lviv", "Odesa", "Kharkiv", "Dnipro", "Donetsk", "Zaporizhzhia", "Luhansk", "Vinnytsia", "Mykolaiv", 
    "Poltava", "Cherkasy", "Chernivtsi", "Ivano-Frankivsk", "Ternopil", "Sumy", "Zhytomyr", "Kropyvnytskyi", 
    "Kherson", "Rivne", "Chernihiv", "Khmelnytskyi", "Kramatorsk", "Mariupol"
]  

@app.route("/")
def index():
    weather_report = "" 

    for city in CITIES:
        URL = f"http://api.openweathermap.org/data/2.5/weather?q={city},UA&appid={API_KEY}&units=metric"
        
        response = requests.get(URL)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            weather_report += f"Температура в {city}: {temp}°C, {weather}<br>"
        else:
            weather_report += f"Ошибка для города {city}: {data}<br>"

    return weather_report  

if __name__ == '__main__':
    app.run(debug=True)
