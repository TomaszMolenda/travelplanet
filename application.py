from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    user = {'username': 'Miguel'}
    return render_template('index.html', user=user)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
