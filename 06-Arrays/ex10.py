int = [0,1,2,3,4,5,6,7,8,9]
numberofodd = 0
numberofeven = 0
i = 0
while i<10:
    if int[i]%2 == 0:
        numberofodd +=1
    else:
        numberofeven+=1
    i+=1

print(numberofodd,numberofeven)