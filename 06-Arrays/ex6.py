arr = [2,3,7,5,4]
#a
print('array', arr)
#b
print('length', len(arr))
#c
print(arr[0])
#d [2,3,7,5,4]
print(arr[1])
#e
print('last',arr[len(arr)-1])
#f
print(arr[len(arr)-2])
#g [2,3,7,5,4]
print(arr[0] + arr[len(arr)-1])
#h
print(arr[len(arr)//2])
#i
for i in arr:
    print(i, end=" ")
#j
print()
for i in range(0,len(arr)//2 + 1):
    print(arr[i], end=" ")