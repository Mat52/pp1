

def compare(array1, array2):
    if(array1 == array2):
        return True
    else:
        return False
print(["water","book","sky"])
print(["water","book","sky"])
print(compare(["water","book","sky"],["water","book","sky"]))
print()
print([True,False])
print([True,False,True])
print(compare([True,False], [True,False,True]))
print()
print([5,3,1])
print([5,3,1])
print(compare([5,3,1],[5,3,1]))
print()

print([3,2,1])
print([3,2])
print(compare([3,2,1],[3,2]))