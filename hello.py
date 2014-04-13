from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from twython import Twython
import json
import imaplib
import re

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
tweets = twitter.search(q='LVHack', count=100, result_type='recent')

# GMAIL API Setup
# Note every hour need to change oauth key
class gmail:
    def __init__(self):
        self.IMAP_SERVER = 'imap.gmail.com'
        self.IMAP_PORT = 993
        self.M = None
        self.mailboxes = None
        self.response = None

    def login(self, username, password):
        self.M = imaplib.IMAP4_SSL(self.IMAP_SERVER, self.IMAP_PORT)
        return_code, self.response = self.M.login(username, password)
        return return_code

    def logout(self):
        self.M.logout()

    def get_mailboxes(self):
        return_code, self.response = self.M.list()
        for item in self.response:
            self.mailboxes.append(item.split()[-1])
        return rc

    def get_mail_count(self, folder='Inbox'):
        return_code, count = self.M.select(folder)
        return count[0]

    def get_unread_count(self, folder='Inbox'):
        return_code, message = self.M.status(folder, "(UNSEEN)")
        unreadCount = re.search("UNSEEN (\d+)", message[0]).group(1)
        return unreadCount

# routing
@app.route('/')
def index():
    return 'Hello World! Why are you here?'

@app.route('/twitter/<query>')
def twitter(query):
    return json.dumps(tweets)

@app.route('/gmail/unread')
def gmailRequest():
    g = gmail()
    g.login(request.args.get('username'), request.args.get('password'))
    return g.get_unread_count()

@app.route('/oauth2callback')
def callback():
    return request.args.get('code')
