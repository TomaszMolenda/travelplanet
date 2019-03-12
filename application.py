from flask import Flask, render_template

import email_sender
from scheduler import run_scheduler
import database

app = Flask(__name__)


@app.route('/')
def hello():
    counter = database.Database.getInstance().fetch_counter()
    founded = database.Database.getInstance().fetch_founded()
    price = database.Database.getInstance().fetch_price()
    return render_template('index.html', price=price, counter=counter, founded=founded)


@app.route('/all')
def all():
    countries = database.Database.getInstance().fetch()
    return render_template('all.html', countries=countries)


@app.route('/send')
def hello1():
    email_sender.send("test")
    return "send"


run_scheduler()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
