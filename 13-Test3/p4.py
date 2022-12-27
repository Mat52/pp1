

def f(d):
    carsin = []
    for car in d:
        if (car[1] == "in"):
            carsin.append(car[0])
        else:
            carsin.remove(car[0])
    carsin.sort()
    return carsin


cars = [["KR234", "in"], ["BA123", "in"], ["GX444", "in"], [
    "KR234", "out"], ["BA111", "in"], ["BA123", "out"], ["KR234", "in"]]

print(f(cars))
