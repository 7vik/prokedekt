from PIL import Image, ImageEnhance
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
from nltk.corpus import wordnet
import cv2

def setContrast(contrast, image_file_path, output_file_path):
    im = Image.open(image_file_path)
    enhancer = ImageEnhance.Contrast(im)
    enhanced_im = enhancer.enhance(contrast)
    enhanced_im.save(output_file_path)

def grayScale(image_file_path, output_file_path):
    image = cv2.imread(image_file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,th3 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
    cv2.imwrite(output_file_path, th3)
