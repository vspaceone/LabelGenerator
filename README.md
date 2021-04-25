[![Build Status](https://jenkins.vspace.one/buildStatus/icon?job=vspaceone%2FLabelGenerator%2Ffeature%252Fjenkins-build-script)](https://jenkins.vspace.one/job/vspaceone/job/LabelGenerator/job/feature%252Fjenkins-build-script/)
[![Docker Image](https://badgen.net/badge/image/available/green?icon=docker)](https://packages.vspace.one/#browse/search/docker=attributes.docker.imageName%3Dlabelgenerator)
# vspace.one e.V. LabelGenerator
The LabelGenerator is a simple webapp, build with Flask. It serves png and jpeg image of our labels with dynamic strings on it. You can choose any name/string just via the path to the image. Find a running instance here: [labelgenerator.vspace.one](labelgenerator.vspace.one). 

## API Access
Make requests to 
```
GET http(s)://example.org/<labelname>/<your_name>.png
```
or
```
GET http(s)://example.org/<labelname>/<your_name>.jpeg
```
to receive the requested label as image.

## Install locally
```
python -m venv .venv
source .venv/bin/activate
pip install opencv-python flask
```

### Run the commandline tool
The Label Generator can be run as commandline tool. Execute:
```
source .venv/bin/activate
python cmdInterface.py -o <outputfile> -t <text> -l <label>
```
Alternative opts are `-h` for help and `-v` for version.

### Run the server
The more common use case is to run the Label Generator as a Webapplication. There for run the following:
```
source .venv/bin/activate
python server.py -p <port> -i <hostip> -d <debug>
```
The default port is `5007`, the default host ip is `0.0.0.0`. Both can be overwritten via opts. The debug flag is either 1 or 0. 

**TODO**: Alternative opts are `-h` for help and `-v` for version.

## Install as Docker Container
Beside running LabelGenerator locally you can deploy it as Docker Container. Therefore run the following:
```
docker build -t labelgenerator .
docker run -d -p 5007:5007 labelgenerator
```

