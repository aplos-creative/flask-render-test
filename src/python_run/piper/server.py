from flask import Flask
app = Flask(__name__)

from .download import getVoices
from . import PiperVoice

@app.route('/server')
def server():
    return 'Server is running!'
