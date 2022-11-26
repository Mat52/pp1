f = open("samp.txt", "r")
wiersze = f.readlines()
print(wiersze)
for i in range(0, len(wiersze)):
    print(i , wiersze[i].strip())
    if (i % 5 == 0 and i != 0):
        input()
