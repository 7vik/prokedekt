from prokedekt.accuracy import accuracy
from prokedekt.img2str import img2string
from prokedekt.imgEnhance import setContrast, grayScale

if __name__ == "__main__":
    total_acc = 0
    total_nums = 0
    img1 = "/Users/satvikgolechha/prokedekt/images/demo3.jpg"
    #for i in range(1,20):
    #    img = img1+str(i)+".jpg"
    grayScale(img1,"demotemp3.jpg")
    setContrast(1,"demotemp3.jpg","demotemp3.jpg")
    #    try:
    #        total_acc += accuracy(img2string("tempestee.jpg", "tempestee.txt"))
    #    except TypeError:
    #        pass
    #    total_nums += 1

    #### 0361

    print(accuracy(img2string("demotemp3.jpg", "demotemp3.txt")))