import math


class C:
    def __init__(self, dict):
        self.dict = dict

    def m(self, n):
        arr = []
        students = self.dict
        for student in students:
            avg = sum(students[student]) / len(students[student])
            if avg >= n:
                arr.append(student)
        arr.sort()
        output = ""
        for name in arr:
            output += "," + name
        output = output[1::]
        return output


s = C({"Peter": [4, 5, 4], "Harry": [2, 5], "Barbara": [3, 3, 3, 5, 5, 5]})
print(s.m(4))
print(s.m(3))
print(s.m(5))
