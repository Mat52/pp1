arr = [12, 6, 4, 9, 10]

def star(n):
    stars = ""
    for i in range(0, n):
        stars+= "*"
    return stars

for i in range(0, len(arr)):
    print(f'{arr[i]}: {star(arr[i])}')
    print()
