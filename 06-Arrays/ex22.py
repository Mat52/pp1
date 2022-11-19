arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
a = 1
for i in range(0, len(arr1)):
    if arr2.__contains__(arr1[i]):
        a = 0
    else:
        print(arr1[i])
        