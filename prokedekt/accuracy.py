# Tells the accuracy of the OCR using English / Tagging (percentage)
from nltk.corpus import wordnet


def accuracy(text="hi", tagged=False, tag="hi"):
    if not tagged:
        low = text.split(' ')
        total = 0
        eng = 0
        for word in low:
            if wordnet.synsets(word):
                eng += 1
            total += 1
        print((eng/total)*100)
    else:
        # tagged
        taglist = tag.split(' ')
        low = text.split(' ')
        total = 0
        eng = 0
        for word in low:
            if word in taglist:
                eng += 1
            total += 1
        print((eng/total)*100)
    return



