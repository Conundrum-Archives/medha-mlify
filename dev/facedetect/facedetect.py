import cv2
import sys
import math
import os
import site
import os.path

classifier = {
  "frontalface": {
    "file": "haarcascade_frontalface_default.xml"
  }
}

faceclassifier = os.path.join(site.getsitepackages()[-1], "cv2", "data", classifier["frontalface"]["file"])
if (not os.path.isfile(faceclassifier)):
  raise FileNotFoundError("cv2 classifiers does not exist in path: {filepath}".format(filepath=faceclassifier))

classifier["frontalface"]["model"] = cv2.CascadeClassifier(faceclassifier)

video_capture = cv2.VideoCapture(0)

ret, frame = video_capture.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = classifier["frontalface"]["model"].detectMultiScale(
  gray,
  scaleFactor=1.1,
  minNeighbors=5,
  minSize=(30, 30),
  flags = cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in faces:
  cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
  distancei = math.floor(((2*3.14 * 180)/(w+h*360)*1000 + 3)*2.54)
  cv2.putText(frame, str(distancei), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

cv2.imwrite("face.png", frame)
