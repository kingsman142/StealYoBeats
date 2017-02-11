from flask import Flask
from twython import Twython
import ConfigParser
import json

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

CONSUMER_KEY = Config.get('TwitterAPI', 'APIKey')
CONSUMER_SECRET = Config.get('TwitterAPI', 'APISecret')
ACCESS_KEY = Config.get('TwitterAPI', 'AccessKey')
ACCESS_SECRET = Config.get('TwitterAPI', 'AccessSecret')

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

app = Flask(__name__)

@app.route("/")
def run():
    return "Running"

@app.route("/generate/<username>")
def generate(username):
    result = ""
    tweets = twitter.get_user_timeline(screen_name=username, count=200, include_rts=False)
    for tweet in tweets:
        result += tweet['text'] + "\n"
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0')
