import urllib.request
f = open("links.txt", "r")
links = f.read()
count = 1
for link in links.split('\n'):
    urllib.request.urlretrieve(link, str(count)+".jpg")
    count += 1