import os
import sys
import cv2
import math
import site
import os.path

class simpleFaceDetect:

  def __init__(self):
    cascadeFile = os.path.join(site.getsitepackages()[-1], "cv2", "data", "haarcascade_frontalface_default.xml")
    if not os.path.isfile(cascadeFile):
      raise FileNotFoundError("cv2 classifier not found in path: {filepath}".format(filepath=cascadeFile))

    self.CascadeClassifier = cv2.CascadeClassifier(cascadeFile)

  def detect(self, imageFrame, calculatedistance=True, labelonimage=False, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE) -> dict:
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
