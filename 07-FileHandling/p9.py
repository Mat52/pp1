f = open("numbers.txt", "r")
sum = 0
wiersze = f.readlines()
for linia in wiersze:
    sum += int(linia.strip())
print(sum)