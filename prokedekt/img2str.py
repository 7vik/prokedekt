from PIL import Image, ImageEnhance
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
from nltk.corpus import wordnet

def img2string(image_file_path, text_file_path="temp.txt", enhanced=False):
    out = open(text_file_path, "w") 
    img = Image.open(image_file_path)
    text = str(pytesseract.image_to_string(img)) 
    out.write(text)
    if enhanced:
        os.remove(image_file_path)
    out.close()
    return text

