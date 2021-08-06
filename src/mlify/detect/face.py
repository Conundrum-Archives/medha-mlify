import os
import sys
import cv2
import math
import site
import os.path

class simpleFaceDetect:

  def __init__(self):
    """initializes cv2 for haarcascade_frontalface_default classifier cml file"""
    cascadeFile = os.path.join(site.getsitepackages()[-1], "cv2", "data", "haarcascade_frontalface_default.xml")
    if not os.path.isfile(cascadeFile):
      raise FileNotFoundError("cv2 classifier not found in path: {filepath}".format(filepath=cascadeFile))
    self.CascadeClassifier = cv2.CascadeClassifier(cascadeFile)

  def detect(self, imageFrame, calculatedistance=True, labelonimage=False, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE) -> dict:
    """
      detects face or faces in provided image frame
      returns JSONObject with keys:
        detected: array of faces-detected - coordinates and size
        labeledimage (if flag enabled): same imageframe with label of detected face(s) on the image frame
        distance (if flag enabled): approx distance of detected face from camera(in cm). calculation based on simple distance calculator.
    """

    returndata = {
      "detected": self.CascadeClassifier.detectMultiScale(
        cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY),
        scaleFactor=scaleFactor,
        minNeighbors=minNeighbors,
        minSize=minSize,
        flags = flags
      )
    }

    for (x, y, w, h) in returndata["detected"]:
      if labelonimage:
        if "labeledimage" not in returndata:
          returndata["labeledimage"] = imageFrame
        returndata["labeledimage"] = cv2.rectangle(returndata["labeledimage"], (x, y), (x + w, y + h), (255, 0, 0), 2)
      if calculatedistance:
        if "distance" not in returndata:
          returndata["distance"] = []
        returndata["distance"].append(math.floor(((2*3.14 * 180)/(w+h*360)*1000 + 3)*2.54))
        if labelonimage:
          returndata["labeledimage"] = cv2.putText(returndata["labeledimage"], str(returndata["distance"][-1]), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return returndata
