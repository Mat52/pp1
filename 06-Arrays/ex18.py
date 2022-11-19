arr = [15, 8, 31, 47, 2, 19]
sum = 0
number = len(arr)

for i in range(0, len(arr)):
    sum += arr[i]
    print(arr[i], end=" ")
print()
print("ar mean", sum/number)