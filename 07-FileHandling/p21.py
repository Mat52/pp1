f = open("powers.txt", "w")

for i in range(1, 11):
    text = str(i) + "," + str(i*i) + "," + str(i*i*i) + "\n"
    f.write(text)