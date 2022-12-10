import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_seasurf import SeaSurf
from flask_talisman import Talisman

load_dotenv()

app = Flask(__name__)

app.secret_key = os.environ['secret_key']

SeaSurf(app)

csp = {
    'default-src': [
        '\'self\'',
        '\'unsafe-inline\'',
        'https://cdn.jsdelivr.net'
    ]
}

Talisman(app, content_security_policy=csp)

api_url = os.environ['api_url']

api_key = os.environ['api_key']
api_host = os.environ['api_host']


def two_day_forecast(city: str):

    querystring = {"q": city, "days": "2"}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": api_host
    }

    response = requests.request(
        "GET", api_url, headers=headers, params=querystring)

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
