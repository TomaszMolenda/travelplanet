from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import database
import time
import atexit
app = Flask(__name__)

database = database.Database()


@app.route('/')
def hello():
    user = {'username': 'Miguel11'}
    counter = database.fetch()
    return render_template('index.html', user=user, counter=counter)


def print_date_time():
    t = time.strftime("%A, %d. %B %Y %I:%M:%S %p")
    print(t)
    database.insert(t)


scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=3)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    app.run(host="0.0.0.0")
