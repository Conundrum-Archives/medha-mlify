import os
import cv2
from pathlib import Path
import mlify.detect.face as df

sdf = df.simpleFaceDetect()

dir_path = os.path.dirname(os.path.realpath(__file__))
faceFile = os.path.join(dir_path, "test-data", "face.jpg")
calogo = os.path.join(dir_path, "test-data", "ca_logo.jpg")

def test_testdatafiles():
  files_to_test = {
    faceFile: {},
    calogo: {}
  }

  for file in files_to_test:
    file = Path(file)
    assert file.exists()

def test_detect_distance():
  """testcase to validate distance function"""
  detImg = sdf.detect(cv2.imread(faceFile), calculatedistance=True, labelonimage=False)
  assert ("distance" in detImg and len(detImg["distance"]) == 1 and detImg["distance"][0] <= 41 and detImg["distance"][0] >= 38)

def test_detect_distanceandlabel():
  """testcase to validate return args when params are changed"""
  detImg = sdf.detect(cv2.imread(faceFile), calculatedistance=True, labelonimage=True)
  assert ("labeledimage" in detImg and "distance" in detImg)

def test_detect_label():
  """testcase to validate return args when params are changed"""
  detImg = sdf.detect(cv2.imread(faceFile), calculatedistance=False, labelonimage=True)
  assert ("labeledimage" in detImg and "distance" not in detImg)


def test_detect_distance():
  """testcase to validate return args when params are changed"""
  detImg = sdf.detect(cv2.imread(faceFile), calculatedistance=False, labelonimage=False)
  assert ("labeledimage" not in detImg and "distance" not in detImg)

def test_detect_noface():
  """testcase to validate no-face case"""
  detImg = sdf.detect(cv2.imread(calogo))
  assert len(detImg["detected"]) == 0
