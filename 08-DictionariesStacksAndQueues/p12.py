import json
film = {
    "nazwa":"Dziennik Noel",
    "premiera": "24.11.2022",
    "produkcja": "USA",
    "gatunek":["Dramat", "Komedia", "Romans", "Świąteczny"],
    "obsada":["Justin Hartley", "Barrett Doss", "Bonnie Bedelia", "James Remar"]
}
out_file = open("favourite.json", "w", encoding="utf-8")
json.dump(film, out_file, indent=4, ensure_ascii=False)
out_file.close()