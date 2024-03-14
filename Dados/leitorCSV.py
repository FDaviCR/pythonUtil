import csv


with open('database.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=';')
    for coluna in leitor:
        print(coluna)
