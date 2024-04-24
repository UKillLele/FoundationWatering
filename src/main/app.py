#!/usr/bin/env python3
import json
from datetime import datetime, timedelta
from flask import Flask, Response
import requests
from flask_sqlalchemy import SQLAlchemy
from prometheus_client import Counter
from sqlalchemy.orm import Mapped, mapped_column

# Create a metric to track the number of requests.
REQUEST_COUNT = Counter('requests_total', 'The total number of requests.')


app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../../../../instance/weather.db"
db = SQLAlchemy(app)


class Weather(db.Model):
    date: Mapped[datetime] = mapped_column(primary_key=True)
    temperature: Mapped[float] = mapped_column(nullable=False)
    precipitation: Mapped[float] = mapped_column(nullable=False)


# Increment the metric each time a request is received.
def handle_request():
    REQUEST_COUNT.inc()


def watering_time(precip, temp):
    if precip > 1:
        return 0
    elif temp < 100:
        return 20
    else:
        return 30


@app.route("/get-watering-time")
def get_watering_time():
    handle_request()
    yesterday = datetime.today() - timedelta(days=1)
    if bool(Weather.query.filter_by(date=yesterday).first()):
        weather: Weather = Weather.query.filter_by(date=yesterday).first()
        return Response(json.dumps(watering_time(weather.precipitation, weather.temperature)), status=200)
    else:
        return Response(json.dumps(watering_time(0, 0)), status=200)


@app.route("/health")
def get_health():
    handle_request()
    return Response("Healthy", status=200)


@app.route("/metrics")
def get_metrics():
    handle_request()
    return Response("request count: " + str(REQUEST_COUNT._value.get()), status=200)


# Start an HTTP server on port 8000 and expose the metrics.
if __name__ == '__main__':
    app.run(port=8000)
