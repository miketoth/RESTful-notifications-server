from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from twython import Twython
import json

app = Flask(__name__)
app.config.from_object(__name__)

APP_KEY = 'U2dIR7IRpydoxaFSUk0hM4ZBZ'
APP_SECRET = 'tb9CIw1yl9wiVXIPvuQ8VmOCpPCAoVfFAUOlM8y0DGp5Z5gU8Y'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

APP_KEY = 'U2dIR7IRpydoxaFSUk0hM4ZBZ'

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

tweets = twitter.search(q='LVHack', count=100, result_type='recent')
#print json.dumps(tweets)


@app.route('/')
def index():
    return 'Hello World'

@app.route('/twitter')
def twitter():
    return json.dumps(tweets)

@app.route('/facebook')
def gmail():
    return 'Fuck gmail'
