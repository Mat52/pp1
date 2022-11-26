f1 = open("MeatAndFish.txt", "r")
f2 = open("GrainsAndBread.txt", "r")
f = open("shoppinglist.txt", "w")

file1 = f1.read()
file2 = f2.read()

f.write(file1)
f.write(file2)
