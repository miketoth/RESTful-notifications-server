from flask import Flask
from TwitterAPI import TwitterAPI

app = Flask(__name__)
api = TwitterAPI('U2dIR7IRpydoxaFSUk0hM4ZBZ','tb9CIw1yl9wiVXIPvuQ8VmOCpPCAoVfFAUOlM8y0DGp5Z5gU8Y','1493725711-ZY9aLfjDcd8n80Q02Sw4HY3Vle3xOvUnCV75JoC','DvUhSD7eikCpgR7RaY3Nzy63Qd4x3OSGBlCPAz0IxgHvI')

@app.route('/')
def hello():
    r = api.request('search/tweets', {'q':'pizza'})
    for item in r.get_iterator():
        return item
