class C:
    @staticmethod
    def m1(n):
        strnumb = str(n)
        new = ""
        for digit in strnumb:
            if(int(digit) % 2 == 0):
                new += digit
        return int(new)

    @staticmethod
    def m2(n):
        strnumb = str(n)
        prev = 0
        for digit in strnumb:
            if(int(digit) >= prev):
                prev = int(digit)
            else:
                return False
        return True

    @staticmethod
    def m3(n):
        retstr = ""
        digs = []
        for dig in str(n):
            digs.append(int(dig))
        for i in range(0, 10):
            if i not in digs:
                retstr += str(i)
        return retstr


print(C.m1(4231564))
print(C.m1(79381))

print(C.m2(125579))
print(C.m2(4557879))

print(C.m3(23557))
print(C.m3(12340))
