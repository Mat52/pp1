import re

f = open("samp.txt", "r")
f = f.readlines()
for wiersz in f:
    words = re.findall("[0-9a-zA-Z]{6,}",wiersz)
    for i in words:
        print(i)


