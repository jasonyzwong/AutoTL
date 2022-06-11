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



#Initialization
filename = "Test Data/testcap2.png"
reader = easyocr.Reader(['ja'])

img = cv2.imread(filename)

#Preprocess 
pre = img
#pre = greyscale(img)
#pre = threshold(pre)


d = pytesseract.image_to_data(pre, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', pre)
cv2.waitKey(0)

