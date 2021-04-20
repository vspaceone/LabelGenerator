# vspace.one e.V. LabelGenerator
The LabelGenerator is a simple webapp, build with Flask. It serves png and jpeg image of our labels with dynamic strings on it. You can choose any name/string just via the path to the image. Find a running instance here: labelgenerator.vspace.one. 

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

