import csv

with open('ejemplo.csv', 'r') as csvfile:
    lector = csv.reader(csvfile, delimiter=";")
    encabezados = next(lector)  # Lee la fila de encabezados
    print(encabezados)
    for fila in lector:
        print(fila)
