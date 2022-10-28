import csv

Naves=[
    ['Nombre', 'Longitud', 'tripulacion'],
    ['Nave de pasajeros C-3','409','290'],
    ['Halcon Milenario',' 34,37','4'],
    ['Nave de aterrizaje C-9979','210','361'],
    ['Crucero ligero MC40a','550','600'],
    ['Estrella de la Muerte','105','1500'],

]


with open ('Naves.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=';')
    #escribir
    writer.writerows(Naves)