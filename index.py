#!/usr/bin/python
from gevent import monkey; monkey.patch_all()

from time import sleep
from bottle import route, run

@route('/v1/hello')
def stream():
    yield 'Hello World!'
    sleep(1)
    yield 'MIDDLE'
    sleep(2)
    yield 'END'

run(host='0.0.0.0', port=8080, server='gevent')
