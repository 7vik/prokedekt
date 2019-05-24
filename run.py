from prokedekt.accuracy import accuracy
from prokedekt.img2str import img2string
from prokedekt.imgEnhance import setContrast

if __name__ == "__main__":
    img1 = "/Users/satvikgolechha/prokedekt/images/lacto.jpg"
    setContrast(2,img1,"temp.jpg")
    accuracy(img2string("temp.jpg"))
