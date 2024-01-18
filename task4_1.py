# # https://www.youtube.com/watch?v=aFNDh5k3SjU
# # part 5.1 Playing Around with Static Images
# # I added a rotated bounding box and make the color red.

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # Define the range of red color in HSV
    lower_red = np.array([0, 100, 50])
    upper_red = np.array([5, 255, 255])
    red_mask = cv.inRange(hsv, lower_red, upper_red)
    # Find contours in the mask
    contours, _ = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # Find the contour with the largest area (largest red object)
    if contours:
        max_contour = max(contours, key=cv.contourArea)
        rect = cv.minAreaRect(max_contour)
        box = cv.boxPoints(rect)
        box = np.int0(box)
        # Draw the rotated bounding box on the frame
        cv.drawContours(frame, [box], 0, (0, 255, 0), 2)
    # Display the resulting frame
    cv.imshow('Red Object Tracking', frame)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

# HSV is usually better because it can handle the light variation in different situation.
# The range is small in hue to track a color but can be large in the saturation and value.

