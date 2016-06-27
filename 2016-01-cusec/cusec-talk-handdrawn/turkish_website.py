#!/usr/bin/python

from flask import Flask, g, request, make_response
import time

app = Flask(__name__)

@app.route('/hello')
@app.route('/')
def index():
    language = request.headers.get('Accept-Language', '')
    if 'en' in language:
        body = "hello world!"
    else:
        body= u"selam d\xfcnya!"
    resp = u"""
    <html>
    <body>
    <h1>{body}</h1>
    </body>
    </html>
    """.format(body=body)
    return make_response(resp)

app.run(port=4000)
