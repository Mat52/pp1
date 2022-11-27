import json

def f(age, course, average):
    ilosc = 0
    f = open('test.json', 'r')
    data = json.loads(f.read())
    for student in data:
        if student['age'] >= age:
            courses = student["studies"]["courses"]
            for course1 in courses:
                if(course1["name"] == course):
                    dlugosc = len(course1["grades"])
                    suma = 0
                    for number in course1["grades"]:
                        suma += number
                    avg = suma / dlugosc
                    if (avg >= average):
                        ilosc += 1
    return ilosc



print(f(21,"statistics", 4))