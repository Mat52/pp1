f = open("numbers.txt","r")
f2 = open("copylines.txt", "w")

wiersze = f.readlines()
for linia in wiersze:
    f2.write(linia)