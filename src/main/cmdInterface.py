
# Author:    Maximilian Noppel
# Date:      April 2021

import getopt
import sys

from labelGenerator import buildImage
from labelGenerator import POSSIBLE_LABELS

from helper import printVersions

def commandlineInterface():
    argv = sys.argv[1:]
 
    opts, args = getopt.getopt(argv, 'vho:t:l:')

    # parse arguments
    outputfile = None
    text = None
    label = None

    for opt in opts:
        if opt[0] == "-o":
            outputfile = opt[1]
        elif opt[0] == "-t":
            text = opt[1]
        elif opt[0] == "-l":
            label = opt[1]
        elif opt[0] == "-v":
            printVersions()
            exit(0)
        elif opt[0] == "-h":
            print("""This is a tool to generate vspace.one e.V. labels with the names of the owners on them.
                \nPlease use the following options:
                -t: Text to print on the label
                -o: Outputfile for the generated image
                -l: Label: owner_only, instructed, documented, public, give_away
                -h: Help
                -v: Print version
                """)
            exit(0)
    
    # validating inputs
    if label is None:
        raise Exception("\nPlease define a label (-l) \n\nPossible labels: \nowner_only\ninstructed\ndocumented\npublic\ngive_away\n")

    if label not in POSSIBLE_LABELS:
        raise Exception(f"\n{l} is a unknown label \n\nPossible labels: \nowner_only\ninstructed\ndocumented\npublic\ngive_away\n")
        
    if text is None and label != "give_away":
        raise Exception("\nPlease provide text via -t")

    # call actual functionality
    buildImage(label,text,outputfile)

if __name__ == "__main__":
    commandlineInterface()    
else:
    print("Please run this file as __main__!")