a = 10
b = 25

for i in range(0, b):
    print("*", end="")
print("")
for i in range(0, a-2):
    print("*", end="")
    for j in range(0, b-2):
        print(" ", end="")
    print("*")
for i in range(0, b):
    print("*", end="")
print("")
