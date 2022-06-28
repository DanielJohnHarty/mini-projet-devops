from flask import Flask
import random
from capitalise import *

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1>Welcome to your capitalising app!</h1>"
if __name__ == "__main__":
    app.run()
