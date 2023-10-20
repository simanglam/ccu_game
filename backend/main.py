from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def handle_get():
    return ''.join(open('./build/index.html').readlines())

@app.route('/', methods = ['POST'])
def handle_post():
    os.system('curl -X POST 127.0.0.1:5000')
    return 'OK'

app.run('127.0.0.1', 3000, True)