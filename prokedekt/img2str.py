from PIL import Image, ImageEnhance
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
from nltk.corpus import wordnet

def img2string(image_file_path, output_file_path, page_number, enhanced=False):
    out = open(output_file_path, "a") 
    img = Image.open(image_file_path)
    text = str(pytesseract.image_to_string(img)) 
    out.write(text)
    if enhanced:
        os.remove(image_file_path)
    out.close()
    return text

