f = open("numbers.txt","r")
f2 = open("copy2.txt", "w")

plik1 = f.read()

f2.write(plik1)