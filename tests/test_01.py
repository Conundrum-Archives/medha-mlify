import os
import cv2
from pathlib import Path
import mlify.detect.face as df

sdf = df.simple_face_detect()

dir_path = os.path.dirname(os.path.realpath(__file__))
face_file = os.path.join(dir_path, "test-data", "face.jpg")
ca_logo = os.path.join(dir_path, "test-data", "ca_logo.jpg")

def test_testdatafiles():
  files_to_test = {
    face_file: {},
    ca_logo: {}
  }

  for file in files_to_test:
    file = Path(file)
    assert file.exists()

def test_detect_distance():
  """testcase to validate distance function"""
  det_img = sdf.detect(cv2.imread(face_file), calculatedistance=True, labelonimage=False)
  assert ("distance" in det_img and len(det_img["distance"]) == 1 and det_img["distance"][0] <= 41 and det_img["distance"][0] >= 38)

def test_detect_distanceandlabel():
  """testcase to validate return args when params are changed"""
  det_img = sdf.detect(cv2.imread(face_file), calculatedistance=True, labelonimage=True)
  assert ("labeledimage" in det_img and "distance" in det_img)

def test_detect_label():
  """testcase to validate return args when params are changed"""
  det_img = sdf.detect(cv2.imread(face_file), calculatedistance=False, labelonimage=True)
  assert ("labeledimage" in det_img and "distance" not in det_img)


def test_detect_distance():
  """testcase to validate return args when params are changed"""
  det_img = sdf.detect(cv2.imread(face_file), calculatedistance=False, labelonimage=False)
  assert ("labeledimage" not in det_img and "distance" not in det_img)

def test_detect_noface():
  """testcase to validate no-face case"""
  det_img = sdf.detect(cv2.imread(ca_logo))
  assert len(det_img["detected"]) == 0
