arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
length = 0
word = ""
for i in range(0, len(arr)):
    if(len(arr[i]) > length):
        length = len(arr[i])
        word = arr[i]
print(word)
