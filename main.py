
import cv2
import numpy as np
import matplotlib.pyplot as plt

# PROJECT: Road Lane and Airport Runway Line Detection

# STEP 1: Check OpenCV installation
print("Road Lane Detection Project Starting!")
print("OpenCV Version:", cv2.__version__)

# STEP 2: Read the road image
image = cv2.imread("images/road.jpg")

if image is None:
    print("Image could not be loaded!")

else:
    print("Image loaded successfully!")
    print("Image dimensions:", image.shape)

    # STEP 3: Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # STEP 4: Display the original and grayscale images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
