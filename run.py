###usage:
###                 python3 run.py input_dir_path output_dir_path 

from prokedekt.accuracy import accuracy
from prokedekt.img2str import img2string
from prokedekt.imgEnhance import setContrast, grayScale
import os
import sys
import tempfile
from pdf2image import convert_from_path

if __name__ == "__main__":
    pdf_dir = str(sys.argv[1])+"pdf"
    os.chdir(pdf_dir)
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):
            pages = convert_from_path(pdf_dir+"/"+pdf_file, 500)
            pdf_file = pdf_file[:-4]
            out_dir = str(sys.argv[2])+"pdf/"+str(pdf_file)
            os.mkdir(out_dir)
            os.chdir(out_dir)
            index = 0
            for page in pages:
                page.save(str(index)+".jpg","JPEG")
                index += 1
    
    for pdf_folder in os.listdir(str(sys.argv[2])+"pdf/"):
        folder = str(sys.argv[2])+"pdf/"+pdf_folder+"/"
        pn = 0
        for num in range(os.listdir(folder).__len__()):
            img2string(folder+str(num)+".jpg", str(sys.argv[2])+"pdf/"+pdf_folder+".txt", pn)
            pn += 1
            os.remove(folder+str(num)+".jpg")
        os.rmdir(folder)
    ##### 0361