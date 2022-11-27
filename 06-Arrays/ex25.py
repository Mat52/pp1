def occurs(number, array):
    if number in array:
        return True
    return False

print(occurs(int(input("Podaj liczbę")), [15,38,7,23,14]))