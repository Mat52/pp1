class Utwor():
    def __init__(self, artysta, tytul, album, rok):
        self.artysta = artysta,
        self.tytul = tytul,
        self.album = album,
        self.rok = rok
        
    def __str__(self):
        return f"Wykonawca: {self.artysta}\nUtwór:{self.tytul}\nAlbum: {self.album}\nRok:{self.rok}"

utwor1 = Utwor("Ed Sheeran","Hearts Don't Break Around Here","Divide","2017")
print(utwor1)
utwor2 = Utwor("Kizo","Disney","Jeszcze 5 minut","2021")
print(utwor2)
utwor3 = Utwor("Sanah", "Szampan", "Królowa Dram", "2020")
print(utwor3)