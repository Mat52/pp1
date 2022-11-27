def minmax(array):
    minimum = min(array)
    maximum = max(array)
    newarr = []
    newarr.append(minimum)
    newarr.append(maximum)
    return newarr

print(minmax([4,2,8,4,7,9,5]))