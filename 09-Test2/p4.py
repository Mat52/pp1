def f(dictionary,x,y):
    sum = 0
    left = x
    right = y

    for i in range(0, len(dictionary)):
        for j in range (0, len(dictionary["arr" + str((i+1))])):
            number = dictionary["arr" + str((i+1))][j]
            if(number >= left and number <= right):
                sum += number
    return sum

    


    




print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))
print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10))