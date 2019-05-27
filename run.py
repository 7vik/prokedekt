from prokedekt.accuracy import accuracy
from prokedekt.img2str import img2string
from prokedekt.imgEnhance import setContrast

if __name__ == "__main__":
    total_acc = 0
    total_nums = 0
    img1 = "/Users/satvikgolechha/prokedekt/estee/images/"
    for i in range(1,20):
        img = img1+str(i)+".jpg"
        setContrast(1.5,img,"tempestee.jpg")
        try:
            total_acc += accuracy(img2string("tempestee.jpg", "tempestee.txt"))
        except TypeError:
            pass
        total_nums += 1
    print(total_acc/total_nums)