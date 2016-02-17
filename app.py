from flask import Flask, redirect
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    now = datetime.now()
    return redirect('http://panmax.love/')

if __name__ == '__main__':
    app.debug = True
    app.run()
