import requests
from flask import Flask, render_template, request

app = Flask(__name__)


def get_current_weather_report(city: str):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": city}

    headers = {
        "X-RapidAPI-Key": "5aebfe91bamsh1532d00e7634804p168ad6jsn9d73ee4e86f6",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()


def two_day_forecast(city: str):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q": city, "days": "2"}

    headers = {
        "X-RapidAPI-Key": "5aebfe91bamsh1532d00e7634804p168ad6jsn9d73ee4e86f6",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()


@app.route("/", methods=['GET', 'POST'])
def main():
    data = None
    if request.method == 'GET':
        return render_template('base.html')
    if request.method == 'POST':
        city = request.form.get('city')
        data = two_day_forecast(city)
        return render_template('index.html', data=data)

