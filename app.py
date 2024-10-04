from flask import Flask
import sys
sys.path.insert(0,'/opt/flask-app')

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
