filename = input("Podaj nazwe pliku ")

f = open(filename, "r")
wiersze = f.readlines()
print(len(wiersze))