from PIL import Image, ImageEnhance
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
from nltk.corpus import wordnet

pdfile = "e.pdf"
pages = convert_from_path(pdfile, 500) 
image_counter = 1

for page in pages: 
    filename = "f_"+str(image_counter)+".jpg"
    page.save(filename, 'JPEG') 
    image_counter = image_counter + 1

filelimit = image_counter-1
outfile = "cosmetics_low_contrast.txt"
f = open(outfile, "w") 

for i in range(1, filelimit + 1): 
    filename = "f_"+str(i)+".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename))))) 
    listofwords = text.split(' ')
    for word in listofwords:
        if wordnet.synsets(word):
            f.write(word+'\n')
    f.write("\n"+"_____________________________________________________________________")
f.close()
