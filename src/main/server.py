
# Author:    Maximilian Noppel
# Date:      April 2021

import base64
import getopt
import sys

import flask
import cv2


from labelGenerator import buildImage
from labelGenerator import POSSIBLE_LABELS

from helper import getVersion


app = flask.Flask(__name__)

def generate(label,text,fileformat):
    label = flask.escape(label)
    text = flask.escape(text)

    fileformats = ["png","jpeg"]
    if fileformat not in fileformats:
        raise Exception("Unknown fileformat ",fileformat)
    
    # validate inputs
    if label not in POSSIBLE_LABELS:
        raise Exception("Label "+label+" not found! Only given_away, instructed, public, owner_only and documented are possible labels!")
        
    # generate image
    img = buildImage(label,text)
    if img is None:
        print("Image is none!")

    # return image png
    retval, buffer = cv2.imencode("."+fileformat, img)
    response = flask.make_response(buffer.tostring())
    response.headers['Content-Type'] = "image/"+fileformat
    return response

@app.route('/<label>/<text>.png', methods=['GET'])
def serverPNG(label,text):
    return generate(label,text,"png")

@app.route('/<label>/.png', methods=['GET'])
def serverPNGEmpty(label):
    return generate(label,"","png")

@app.route('/<label>/<text>.jpeg', methods=['GET'])
def serverJPEG(label,text):
    return generate(label,text,"jpeg")

@app.route('/<label>/.jpeg', methods=['GET'])
def serverJPEGEmpty(label):
    return generate(label,"","jpeg")

@app.route('/', methods=['GET'])
def serverIndex():
    resp = flask.make_response(flask.render_template('index.html', version=getVersion()), 200)
    resp.headers["Content-type"] = "text/html; charset=utf-8"
    return resp

if __name__ == '__main__':
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, 'vhp:i:d:')

    # parse arguments
    port = 5007
    ip = "127.0.0.1"
    debug = False
    print(opts)

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