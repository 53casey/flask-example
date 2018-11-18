from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Stra'


@app.route('/test/<foo>')
def new_name(foo):
    answer = "Hello " + foo + "!!!"
    return answer
