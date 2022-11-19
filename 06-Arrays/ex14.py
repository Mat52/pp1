arr = [[True,False],[True,True],[False,False]]

for i in range(0,len(arr)):
    for j in range (0, len(arr[i])):
        if (arr[i][j] == True):
            arr[i][j] = False
        else:
            arr[i][j] = True
print(arr)