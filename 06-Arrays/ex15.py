arr = [[0,0,0],[0,0,0],[0,0,0]]

a=0
for i in range (0, len(arr)):
    arr[i][a] = 1
    a+=1
    for j in arr[i]:
        print(j, end=" ")
    print()

        
