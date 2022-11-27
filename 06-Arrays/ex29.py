def f(arr, number):
    sum = 0
    for i in arr:
        if number <= i:
            sum += 1
    return sum


print(f([2.5,4.3,5.6],float(input("Podaj liczbę rzeczywistą"))))