
# Author:    Maximilian Noppel
# Date:      April 2021

import cv2

def printVersions():
    print(f"LabelGenerator : v0.0.1")
    print(f"opencv2 version: {cv2.__version__}")



if __name__ == "__main__":
    print("""Please run the commandline interface (cmtInterface.py) as __main__ 
    or the server.py file as Flask application. This file is just a source file!""")