arr = [15, 8, 31, 47, 2, 19]
sum = 0
number = len(arr)
i = 0
while i < len(arr):
    sum += arr[i]
    print(arr[i], end=" ")
    i+=1
print()
print("ar mean", sum/number)