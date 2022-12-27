class C:
    def __init__(self, object):
        self.object = object

    def __str__(self) -> str:
        sum = 0
        string = ""
        for i in range(0, len(self.object)):
            sum += self.object[i]
            string += "+"
            string += str(self.object[i])
        string += "="
        string += str(sum)
        string = string[1::]
        return(string)


print(C([5, 12]))
print(C([6, 0, 15]))
