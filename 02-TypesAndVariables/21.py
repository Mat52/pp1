import random
dice = random.randint(1, 6)
useranswer = int(input("Zgadnij jaka kostka wypadła "))

print(dice == useranswer)
