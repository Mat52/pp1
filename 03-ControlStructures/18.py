amount = int(input("Enter the amount in PLN: "))
liczba5 = int(amount/5)
reszta1 = amount % 5
liczba2 = int(reszta1/2)
reszta2 = liczba2 % 2
liczba1 = int(reszta2)
print("The amount of PLN 18 in conins:")
print(f"5 zł - {liczba5}")
print(f"2 zł - {liczba2}")
print(f"1 zł - {liczba1}")
