x = int(input("Podaj wartość współrzędnej x: "))
y = int(input("Podaj wartość współrzędnej y: "))
print(f"x = {x}")
print(f"y = {y}")
if (x == 0 and y == 0):
    print(
        f"Point P ({x},{y}) is in the position (0,0) of the coordinate system")
if (x == 0 and y != 0):
    print(f"Point P ({x},{y}) is located on y axis")
if (x != 0 and y == 0):
    print(f"Point P ({x},{y}) is located on x axis")
if (x > 0 and y > 0):
    print(f"Point P ({x},{y}) is located in 1 quadrant of coordinate system")
if (x > 0 and y < 0):
    print(f"Point P ({x},{y}) is located in 2 quadrant of coordinate system")
if (x < 0 and y < 0):
    print(f"Point P ({x},{y}) is located in 3 quadrant of coordinate system")
if (x < 0 and y > 0):
    print(f"Point P ({x},{y}) is located in 3 quadrant of coordinate system")
