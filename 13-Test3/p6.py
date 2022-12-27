class C:
    def __init__(self, v):
        self.v = v

    def m1(self):
        return (self.v)

    def m2(self):
        self.v += 1

    def m3(self):
        self.v -= 1

    def m4(self, n):
        self.v += n


c = C(5)
print(c.m1())
c.m2()
print(c.m1())
c.m4(-8)
print(c.m1())
c.m3()
print(c.m1())
c.m4(10)
print(c.m1())
