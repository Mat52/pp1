import math
a = float(input("Podaj bok a "))
b = float(input("Podaj bok b "))
c = float(input("Podaj bok c "))

print(a, b, c)
p = float(((a+b+c)/2))
pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(pole)
