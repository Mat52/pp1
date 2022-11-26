def f(human_age):
    dogage = 0
    for i in range(1,human_age + 1):
        if (i == 1 or i ==2):
            dogage += 10
        else:
            dogage +=4
    return dogage


print(f(15))
print(f(2))