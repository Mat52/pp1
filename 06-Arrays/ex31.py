def f(array):
    newarr = []
    for i in array:
        if (i % 2 == 1):
            newarr.append(i)
    for i in array:
        if (i % 2 == 0):
            newarr.append(i)
    return newarr

print(f([0,1,2,3,4,5,6,7,8,9]))