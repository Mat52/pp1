def bubblesort(array):
    swapped = False
    for n in range(len(array)-1, 0, -1):
        for i in range(n):
            if array[i]> array[i+1]:
                swapped = True
                array[i], array[i+1]= array[i+1], array[i]
        if not swapped:
            return
array = [1,4,2,3]
bubblesort(array)
print(array)