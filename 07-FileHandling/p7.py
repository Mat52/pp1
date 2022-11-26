f = open("countries.txt", "r")
i = 1
for line in f:
    print(i, end =" ")
    print(line, end="")
    i+=1
