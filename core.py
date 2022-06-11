from cv2 import COLOR_BGR2GRAY
import easyocr
import cv2
import pytesseract
from pytesseract import Output

#Functions
def greyscale(image):
  return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def noise(image):
  return cv2.medianBlur(image, 5)

def threshold(image):
   return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def speechBubbles(image):
  imageGrayBlurCanny = cv2.Canny(image,50,500)
  binary = cv2.threshold(imageGrayBlurCanny,235,255,cv2.THRESH_BINARY)[1]
  contours = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
  croppedImageList = []
  for contour in contours:
    rect = cv2.boundingRect(contour)
    [x, y, w, h] = rect
    if w < 500 and w > 60 and h < 500 and h > 25:
      croppedImage = image[y:y+h, x:x+w]
      croppedImageList.append(croppedImage)
  return croppedImageList

#Initialization
filename = "Test Data/005.jpg"
reader = easyocr.Reader(['ja'])

img = cv2.imread(filename)

#Preprocess 
bubbles = speechBubbles(img)

for bubble in bubbles:
  cv2.imshow('image', bubble)
  cv2.waitKey()

