from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    retutn 'Privet'


app.run(port='8000')
