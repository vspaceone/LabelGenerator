
# Author:    Maximilian Noppel
# Date:      April 2021


import getopt
import sys
import os
import pathlib

import flask
from flask_caching import Cache
import cv2

from LabelGenerator import LabelGenerator
from Helper import getVersion



app = flask.Flask(__name__)
cache = Cache(config={
    'CACHE_TYPE': 'FileSystemCache',
    'CACHE_DEFAULT_TIMEOUT': 60*60*24*3, # cache for 3 days
    'CACHE_THRESHOLD': 500, # cache max. 500 items
    'CACHE_DIR': 'cache'
})

cache.init_app(app)

def generate(label,text,fileformat):
    lg = LabelGenerator()
    fileformats = ["png","jpeg"]
    if fileformat not in fileformats:
        raise Exception("Unknown fileformat ",fileformat)
    
    # validate inputs
    if label not in lg.POSSIBLE_LABELS:
        raise Exception("Label "+label+" not found! Only given_away, instructed, public, owner_only, documented, hackable and not_applicable are possible labels!")
        
    # generate image
    img = lg.buildImage(label,text)
    if img is None:
        raise Exception("Image is none!")

    # return image png
    retval, buffer = cv2.imencode("."+fileformat, img)
    response = flask.make_response(buffer.tostring())
    response.headers['Content-Type'] = "image/"+fileformat
    return response

@app.route('/<label>/<text>.png', methods=['GET'])
@cache.cached()
def serverPNG(label,text):
    return generate(label,text,"png")

@app.route('/<label>/.png', methods=['GET'])
@cache.cached()
def serverPNGEmpty(label):
    return generate(label,"","png")

@app.route('/<label>/<text>.jpeg', methods=['GET'])
@cache.cached()
def serverJPEG(label,text):
    return generate(label,text,"jpeg")

@app.route('/<label>/.jpeg', methods=['GET'])
@cache.cached()
def serverJPEGEmpty(label):
    return generate(label,"","jpeg")

@app.route('/', methods=['GET'])
def serverIndex():
    resp = flask.make_response(flask.render_template('index.html', version=getVersion()), 200)
    resp.headers["Content-type"] = "text/html; charset=utf-8"
    return resp

def startServer():
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, 'vhp:i:d:')

    # parse arguments
    port = 5007
    ip = "0.0.0.0"
    debug = False

    for opt in opts:
        if opt[0] == "-i":
            ip = opt[1]
        elif opt[0] == "-p":
            port = int(opt[1])
        elif opt[0] == "-d":
            debug = int(opt[1])

    print("Running on")
    print("Host: ",ip)
    print("Port: ",port)

    app.run(debug=debug,host=ip,port=port)

if __name__ == '__main__':
    startServer()
