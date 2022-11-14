arr = [[2,5,4],[9,0,3]]

print(arr)
print("number of rows",len(arr))
print("number of columns", len(arr[0]))
print(len(arr), "x", len(arr[0]))
print(arr[0][1])
print(arr[1][2])

print()

for i in range(0, len(arr[1])):
    print(arr[1][i], end = " ")

print()
print()

for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        print(arr[i][j], end= " ")
    print()

print()
for i in range(0, len(arr)):
    print(arr[i][-1])