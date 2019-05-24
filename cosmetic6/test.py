o = "temp.txt"
f = open(o, "a")
for word in "this is a sentence":
    f.write(word+"\n")