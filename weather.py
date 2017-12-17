import os
import forecastio
from flask import Flask, request, Response
from slackclient import SlackClient

FORCAST_TOKEN = 'f66898e038273c6ff4b20480edc4141c'

def forcast():
    lat = 37.5124413
    lng = 126.9540519

    forcast = forecastio.load_forecast(FORCAST_TOKEN,lat,lng)
    byHour = forcast.hourly()

    return byHour.summary

 
