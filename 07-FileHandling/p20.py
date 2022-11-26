import random
f = open("randoms.txt", "w")
for i in range(50):
    f.write(str(random.randint(100,999)) + "\n")