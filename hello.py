from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from twython import Twython
import json

# Flask setup
app = Flask(__name__)
app.config.from_object(__name__)
app.debug=True

# Twitter API Setup
APP_KEY = 'U2dIR7IRpydoxaFSUk0hM4ZBZ'
APP_SECRET = 'tb9CIw1yl9wiVXIPvuQ8VmOCpPCAoVfFAUOlM8y0DGp5Z5gU8Y'
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
APP_KEY = 'U2dIR7IRpydoxaFSUk0hM4ZBZ'
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

# routing
@app.route('/')
def index():
    return 'Hello World! Why are you here?'

@app.route('/twitter/<query>')
def twitter(query):
    tweets = twitter.search(q=query, count=100, result_type='recent')
    return json.dumps(tweets)

@app.route('/gmail')
def gmail():
    return 'Fuck gmail'
