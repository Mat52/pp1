arr = [-15, 8, -31, 47, -2, 19]

for i in range (0, len(arr)):
    if(i == 0):
        min = arr[i]
        max = arr[i]
    else:
        if(arr[i] < min):
            min = arr[i]
        if(arr[i] > max):
            max = arr[i]
print(arr)
print("minimum", min)
print("maximum", max)
        
