from flask import Flask
from twython import Twython
import ConfigParser
import json
import re

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

CONSUMER_KEY = Config.get('TwitterAPI', 'APIKey')
CONSUMER_SECRET = Config.get('TwitterAPI', 'APISecret')
ACCESS_KEY = Config.get('TwitterAPI', 'AccessKey')
ACCESS_SECRET = Config.get('TwitterAPI', 'AccessSecret')

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Running"

@app.route("/generate/<username>")
def generate(username):
    result = ""
    tweets = twitter.get_user_timeline(screen_name=username, count=200, include_rts=False)
    for tweet in tweets:
        content = re.sub(r'(@([a-zA-Z0-9]){1,15} )|((http|https):\/\/t\.co\/([a-zA-Z0-9]){10})', '', tweet['text']) + "\n"
        result += content + "\n"
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0')
