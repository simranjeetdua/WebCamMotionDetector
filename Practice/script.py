# practice script to get familiar with opencv library.

import cv2 #importing the open source computer vision library

img=cv2.imread(r"C:\Users\Simranjeet\Desktop\WebCamMotionDetector\Practice\mountains.jpg",0) #reading the image from the project folder and giving argument as 0 to read the image in grayscale
## problems encountered 1-- None Type - resolution : used the full path name
##                      2-- unicodeescape error - resolution: used "r" before path name to convert it into raw string

print(type(img)) #print the type of the image format stored ie: of a numpy array

print(img) #prints the whole numpy 2d array

print(img.shape) #prints the shape of numpy array

print(img.ndim) #prints the dimension of the array

cv2.imshow("mountains",img) #to show the img in pixels
cv2.waitKey(0) # waits for the time to show the img
cv2.destroyAllWindows() #destroy open windows
