import csv

with open("datacsv.csv", "r") as file:
    reader = csv.reader(file, age<50)
    for row in reader:
        print(row)