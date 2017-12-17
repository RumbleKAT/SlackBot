#-*- coding: utf-8 -*-

import os
import weather
from flask import Flask, request, Response
from slackclient import SlackClient

app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')
SLACK_TOKEN = os.environ.get('SLACK_TOKEN', None)
slack_client = SlackClient(SLACK_TOKEN)

def testApp(message):
    testword = "날씨"
    print(testword)

    if message in testword or message in "weather":
        print("Weather  : " + weather.forcast())
    else:
        print("Error")
    return weather.forcast()

"""
test = testApp("날씨")
print(test)

"""

def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='SecretaryBot',
        icon_url="https://raw.githubusercontent.com/RumbleKAT/SlackBot/master/sana.png"
     )

@app.route('/webhook',methods=['POST'])
def inbound():
    username = request.form.get('user_name')
    if request.form.get('token') == SLACK_WEBHOOK_SECRET and username != 'slackbot':
        channel_name = request.form.get('channel_name')
        channel_id = request.form.get('channel_id')
        username = request.form.get('user_name')
        text = request.form.get('text')
        text = testApp(text)

        send_message(channel_id, text)

    return Response(), 200

@app.route('/',methods=['GET'])
def test():
    return Response("It works!")

if __name__ == "__main__":
    app.run(debug=True)
