film_titles =["Shrek 1", "Shrek 2", "Shrek 3", "Shrek 4", "Shrek 5"]

f = open("films.txt", "w")
for i in film_titles:
    f.write(i + "\n")