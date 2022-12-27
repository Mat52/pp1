def f(n):
    word = ""
    if n < 1:
        return ""
    else:
        for i in range(1, n+1):

            if(i % 5 == 0):
                word += "/-"
            else:
                word += "/"
        if (word[-1] == "-"):
            word = word[:-1]
        return word


print(f(-4))
print(f(0))
print(f(5))
print(f(7))
print(f(10))
print(f(11))
