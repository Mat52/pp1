import random
sum = 0
for i in range(0, 3):
    dice = random.randint(1, 6)
    print(dice)
    sum = sum + dice
print(sum)
