# -*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('baidu.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
