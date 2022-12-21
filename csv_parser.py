import csv
# https://pythonworld.ru/moduli/modul-csv.html


with open('test.csv', 'r', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         print(', '.join(row))