import csv
filas=[]
with open('Naves.csv', newline='') as File:  
    reader = csv.reader(File)
    naves=reader

for i in reader:
    if i[0]=='Nombre':
        keys=i
        del i
    else:
        filas.append(i)


def info(nave):
    nombre=keys.index('Nombre')
    for i in filas:
        if i[nombre]==nave:
            print(i)
info('Halcon Milenario')
info('Estrella de la Muerte')
