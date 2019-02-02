from flask import Flask, render_template
from scheduler import run_scheduler
import database

app = Flask(__name__)


@app.route('/')
def hello():
    user = {'username': 'Miguel11'}
    counter = database.Database.getInstance().fetch_counter()
    founded = database.Database.getInstance().fetch_founded()
    return render_template('index.html', user=user, counter=counter, founded=founded)


run_scheduler()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
