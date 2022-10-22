first = 0
second = 1
print(first, end=" ")
print(second, end=" ")
for i in range(0, 48):
    next = first + second
    first = second
    second = next
    print(next, end=" ")
