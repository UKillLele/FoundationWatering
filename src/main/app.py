#!/usr/bin/env python3
import requests
from datetime import date, datetime, timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column


app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weather.db"
app.app_context().push()
# initialize the app with the extension
db = SQLAlchemy(app)


class Weather(db.Model):
    date: Mapped[datetime] = mapped_column(primary_key=True)
    temperature: Mapped[float] = mapped_column(nullable=False)
    precipitation: Mapped[float] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()

'''
Helper function to get temperature
using API
'''


def check_connection():
    url = "https://api.open-meteo.com/v1/forecast"
    response = requests.get(url)
    return response.status_code


def get_weather():
    if check_connection() == 200:
        yesterday = date.today() - timedelta(days=1)
        url = "https://api.open-meteo.com/v1/forecast?"  # base
        url += "latitude=33.1&longitude=-96.86&"  # location
        url += "daily=temperature_2m_max,precipitation_sum&"  # variables to get
        url += "temperature_unit=fahrenheit&precipitation_unit=inch&timezone=America%2FChicago&"  # units
        url += f"start_date={yesterday}&end_date={yesterday}"  # date
        response = requests.get(url)
        return response.json()["daily"]


'''
In main, we first get the temperature and precipitation and then 
create a new object that we can add to the database. 
'''


if __name__ == "__main__":
    weather = get_weather()
    if weather:
        d, temp, precip = weather["time"][0], weather["temperature_2m_max"][0], weather["precipitation_sum"][0]
        new_entry = Weather(date=datetime.fromisoformat(d), temperature=temp, precipitation=precip)
        existing = bool(Weather.query.filter_by(date=datetime.fromisoformat(d)).first())
        if not existing:
            db.session.add(new_entry)
            db.session.commit()
