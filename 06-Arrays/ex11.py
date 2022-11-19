months = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzien"]
def month(n):
    return months[n-1]

print(month(1))
print(month(2))
print(month(11))
print(month(12))
