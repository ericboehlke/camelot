
# Simple Apriltag tracking demo/example code for MASLAB 2020 CV Lecture

import sys
import cv2
import apriltag
import numpy as np

# CAMERA_INDEX indicates which webcam to use if we have
# multiple connected. If you just have one, use '0'.
CAMERA_INDEX = 0

# cap is a VideoCapture object we can use to get frames from webcam
cap = cv2.VideoCapture(CAMERA_INDEX)

# Initialize an Apriltag Detector
at_detector = apriltag.Detector()

while True:
  # Capture a frame from the webcam
  _, frame = cap.read()
  
  height , width , layers =  frame.shape
  new_h=height//2
  new_w=width//2
  frame = cv2.resize(frame, (new_w, new_h))
  # We need to convert frame to gray scale to be compatible with this library
  bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Look for Apriltags in frame
  tags = at_detector.detect(bw_frame)

  # If we see any...
  if len(tags) != 0:
    print("here we go!")
    # We can just consider the first tag we see
    tag = tags[0]

    # Print out tag ID. We will use distinct tag IDs for the goals and dispensers
    print("Tag ID: {}".format(tag.tag_id))

    # Structure the tag corners as a numpy array just to make it displayable
    corners = np.array(tag.corners, np.int32)
    # Draw a rectangle around the Apriltag on our frame
    cv2.polylines(frame, [corners], True, (0, 255, 0), thickness=5)

  # Display that frame (resized to be smaller for convenience)
  cv2.imshow('frame', frame)

  # Quit if user presses q
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
