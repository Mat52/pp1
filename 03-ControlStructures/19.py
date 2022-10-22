wiekPsa = int(input("Podaj wiek psa: "))
if(wiekPsa < 3):
    if(wiekPsa == 1):
        print("Wiek psa w przeliczeniu na człowieka to 10.5 lat")
    if(wiekPsa == 2):
        print("Wiek psa w przeliczeniu na człowieka to 21 lat")
else:
    wiek = (wiekPsa-2)*4 + 21
    print(f"Wiek psa w przeliczeniu na człowieka to {wiek} lat")
