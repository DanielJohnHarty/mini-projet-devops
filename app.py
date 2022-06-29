
from flask import Flask
import random
from capitalise import *

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1>Welcome to your capitalising app!</h1>"

@app.route("/capitalise/<input_str>")
def capitalise(input_str):
    return f"""
      <h1>Capitalise {input_str}</h1>
      <h2>Capitalise {capital_case(input_str)}</h2>
    """

if __name__ == "__main__":
    app.run()
