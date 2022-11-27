import csv

with open("datacsv.csv", "r") as file:
    fieldnames = ['first_name', "last_name", "age", "gender", "email"]
    reader = csv.DictReader(file, fieldnames = fieldnames)
    i = 0
    for row in reader:
        if i!=0:
            if (int(row["age"]) < 30):
                print(row["first_name"], row["last_name"], row["email"])
        i+=1