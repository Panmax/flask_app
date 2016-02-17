# -*- coding: utf-8 -*-
from flask import Flask, redirect
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return u'你好,星辰大海'

if __name__ == '__main__':
    app.debug = True
    app.run()
