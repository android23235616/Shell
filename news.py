# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:53:12 2017

@author: Tanmay
"""

from flask import Flask

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.errorhandler(404)
def page_not_found(e):
    # your processing here
    return "returning 404"


if __name__ == '__main__':
   app.run(debug = True)

