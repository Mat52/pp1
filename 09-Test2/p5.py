

def f(first_letter, last_letter):
    count = 0
    f = open('test.txt', 'r', encoding="utf-8")
    wiersze = f.readlines()
    for linia in wiersze:
        linijka = linia.strip().split(" ")
        for slowo in linijka:
            if len(slowo)>0:
                if(slowo[0]==first_letter and slowo[-1]==last_letter):
                    count += 1
    return count


print(f("w", "d"))
    