#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/
#https://www.maketecheasier.com/file-permissions-what-does-chmod-777-means/

from flask import Flask, render_template

app = Flask(__name__)

#Static
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

#Dynamic
@app.route('/coucou/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
