#!/usr/bin/env python3

from flask import Flask
import requests

app = Flask(__name__)


def get_watering_time():
    return requests.get("http://127.0.0.1:8000/get-watering-time")


@app.route("/")
def main():
    watering_time = get_watering_time().text
    return f'''
     <div>
        <h1>Should you water your foundation today in The Colony, Texas?</h1>
        <p>You should water your foundation for {watering_time} minutes.
     </div>
     '''
