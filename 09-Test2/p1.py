def f(player1, player2):
    sum1 = 0
    sum2 = 0
    for letter in player1:
        if (letter == "A" or letter == "K" or letter == "Q" or letter == "J" or letter == "T"):
            sum1+=10
        else:
            sum1 = sum1 + int(letter)
    for letter in player2:
        if (letter == "A" or letter == "K" or letter == "Q" or letter == "J" or letter == "T"):
            sum2+=10
        else:
            sum2 = sum2 + int(letter)
    if(sum1 > sum2):
        return True
    else:
        return False

print(f("AJ972", "AQT72"))
print(f("9532", "K8"))
print(f("987", "AT4"))
