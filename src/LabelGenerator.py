
# Author:    Maximilian Noppel
# Date:      April 2021

from enum import IntEnum

import os
import cv2

class LabelGenerator():

    POSSIBLE_LABELS = [
        "owner_only",
        "instructed",
        "documented",
        "public",
        "give_away",
        "not_applicable",
        "hackable"
    ]

    def __init__(self):
        pass

    def buildImage(self, label, text, outputfile=None):


        if label not in self.POSSIBLE_LABELS:
            raise Exception("Label "+label+" unknown!")

        from pathlib import Path
        here = Path(__file__).parent.resolve()

        labelpath = os.path.abspath(os.path.join(here,"..","labels",label+".png"))
        # read in image
        img = cv2.imread(labelpath)
        if img is None:
            raise Exception("Failed to load label "+labelpath)

        # font settings
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontsize = 1.3
        fontthickness = 3
        textsize = cv2.getTextSize(text, font, fontsize, fontthickness)[0]

        # rescale if to big
        while textsize[0] > img.shape[1] - 4:
            fontsize -= 0.1
            textsize = cv2.getTextSize(text, font, fontsize, fontthickness)[0]

        # get coords based on boundary
        textX = int( (img.shape[1] - textsize[0]) / 2)
        textY = int( 130)

        # add text centered on image
        cv2.putText(img, text, (textX, textY ), font, fontsize, (0, 0, 0), fontthickness)

        if outputfile is not None:
            cv2.imwrite(outputfile,img)

        return img


if __name__ == "__main__":
    print("""Please run the commandline interface (testCMDInterface.py) as __main__ 
    or the Server.py file as Flask application. This file is just a source file!""")
