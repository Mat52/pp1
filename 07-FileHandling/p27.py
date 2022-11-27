f = open("grades.txt", "r")
wiersze = f.readlines()

for wiersz in wiersze:
    dane = wiersz.strip().split(" ")
    if (len(dane)> 0):
        if(dane[0] == "Name:"):
            name = dane[1]
            print(name)
        elif(dane[0] == "Grades:"):
            ilosc = len(dane)
            suma = 0
            for i in range (1, len(dane)):
                ocena = dane[i]
                if ocena[-1] == ",":
                    ocena = ocena[:-1]
                ocena = float(ocena)
                suma = suma + ocena
            print("średnia", suma/ilosc)

