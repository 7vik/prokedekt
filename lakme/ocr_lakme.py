from PIL import Image, ImageEnhance
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
from nltk.corpus import wordnet

def removeColour(filename, outimg):
        img =  Image.open(filename).convert('RGB')
        source = img.split()
        R, G, B = 1, 1, 0
        out = source[R].point(lambda i: i * 0)
        source[R].paste(out, None, None)
        img = Image.merge(img.mode, source)
        img.save(outimg)

def black_and_white_dithering(input_image_path,output_image_path,dithering=True):
    color_image = Image.open(input_image_path)
    if dithering:
        bw = color_image.convert('L')  
    else:
        bw = color_image.convert('L',dither=Image.NONE)
    bw.save(output_image_path)

from PIL import Image
 
def rotate(image_path, degrees_to_rotate, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(saved_location)

iteration = 13

outfile = "lakme"+str(iteration)+".txt"
f = open(outfile, "w") 

filename = "lakme.jpg"
outimg = "temp"+str(iteration)+".jpg"
black_and_white_dithering(filename, outimg)
text = str(((pytesseract.image_to_string(Image.open(outimg))))) 
listofwords = text.split(' ')
for word in listofwords:
    f.write(word+'\n')
rotate(outimg, 270, outimg)
text = str(((pytesseract.image_to_string(Image.open(outimg))))) 
listofwords = text.split(' ')
for word in listofwords:
    f.write(word+'\n')
f.close()
