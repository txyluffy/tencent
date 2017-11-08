#!/usr/bin/python
#coding=utf-8

import os

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello World"
