pin = "0805"
proba = 1
pinusera = ""
while proba < 4 and pinusera != pin:
    pinusera = input("Podaj pin: ")
    proba = proba+1
    if(pinusera == pin):
        print("Uzyskano dostęp")
        exit
    else:
        print("Niepoprawny pin")
if(proba > 4):
    print("Twoja karta została zablokowana")
