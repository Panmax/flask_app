from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    now = datetime.now()
    return 'hello world %s' % now

if __name__ == '__main__':
    app.debug = True
    app.run()

