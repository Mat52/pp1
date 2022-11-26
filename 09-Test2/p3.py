def f(array2D):
    sums=[]
    for i in range(0, len(array2D[0])):
        sums.append(0)
    
    for i in range(0, len(array2D)):
        for j in range(0,len(array2D[i])):
            sums[j] += array2D[i][j]
    return sums
    

print(f([[3,6,2,7], [9,5,4,0], [2,8,0,9]]))