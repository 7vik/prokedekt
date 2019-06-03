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
            pages = convert_from_path(pdf_file, 500)
            pdf_file = pdf_file[:-4]
            for page in pages:
                out_dir = str(sys.argv[2])+"pdf"
                os.chdir(out_dir)
                page.save("%s-page%d.jpg" % (pdf_file,pages.index(page)),"JPEG")
    total_acc = 0
    total_nums = 0
    #img1 = "/Users/satvikgolechha/prokedekt/newlakme.jpg"
    ##for i in range(1,20):
    ##    img = img1+str(i)+".jpg"
    #grayScale(img1,"demotemp3.jpg")
    #setContrast(1,"demotemp3.jpg","demotemp3.jpg")
    ##    try:
    ##        total_acc += accuracy(img2string("tempestee.jpg", "tempestee.txt"))
    ##    except TypeError:
    ##        pass
    ##    total_nums += 1
#
    ##### 0361
#
    #print(accuracy(img2string("demotemp3.jpg", "demotemp3.txt")))