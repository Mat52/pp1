arr = [15, 8, 31, 47, 2, 19] 

revarr = []

for i in range(len(arr)-1, -1, -1):
    print(i)
    revarr.append(arr[i])
print("arr", arr)
print("rev arr", revarr)