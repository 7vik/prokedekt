from PIL import Image, ImageEnhance
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
from nltk.corpus import wordnet

def setContrast(contrast, image_file_path, output_file_path):
    im = Image.open(image_file_path)
    enhancer = ImageEnhance.Contrast(im)
    enhanced_im = enhancer.enhance(contrast)
    enhanced_im.save(output_file_path)

