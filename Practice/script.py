# practice script to get familiar with opencv library.

import cv2 #importing the open source computer vision library

img=cv2.imread(r"C:\Users\Simranjeet\Desktop\WebCamMotionDetector\Practice\mountains.jpg",0) #reading(imread==image read) the image from the project folder and giving argument as 0 to read the image in grayscale
## problems encountered 1-- None Type - resolution : used the full path name
##                      2-- unicodeescape error - resolution: used "r" before path name to convert it into raw string

print(type(img)) #print the type of the image format stored ie: of a numpy array

print(img) #prints the whole numpy 2d array

print(img.shape) #prints the shape of numpy array

print(img.ndim) #prints the dimension of the array

resized_img=cv2.resize(img,(500,500)) #resized the image to make it square.

resized_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #resized it half the resolution to not spoil the ratio. keep the dimension[1] first and then the dimension[0]

print(resized_img.shape) #shape of numpy array also changed

cv2.imshow("mountains",resized_img) #to show the img in pixels
cv2.waitKey(0) # waits for the time to show the img, 0== infinite
cv2.destroyAllWindows() #destroy open windows

cv2.imwrite(r"Practice\NewMountains.jpg",resized_img) #imwrite==image write used to write image in the new file
