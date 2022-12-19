class Student:

    university = "UEK KRAKÓW"
    id = 100000
    def __init__(self, name, surname, field):
        self.name = name
        self.surname = surname
        self.field = field
        self.id = Student.id
        Student.id +=1
        
        
    def __str__(self):

        return self.name + " " + self.surname + "," + str(self.id) + ","+ self.field + ", " + self.university

student1 = Student("Anna", "Maj", "Applied Informatics")
print(student1)
student2 = Student("Anna", "Kwiecień", "Applied Informatics")
print(student2)
student3 = Student("Jan", "Czerwiec", "Applied Informatics")
print(student3)


        