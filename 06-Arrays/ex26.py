array = [5,1,9,6,1]
array.sort()
unique = []
for i in array:
    if(i not in unique):
        unique.append(i)
print("second largest: ", unique[-2])
