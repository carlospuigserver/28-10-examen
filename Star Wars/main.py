from Naves import EstrellaMuerte
from Naves import HalconMilenario
from Naves import ATAP
from Naves import CañoneraLAAT
from Naves import ATTE

def toppasajeros(lista):
    contador=50000
    l=lista
    for i in lista:
        if (i.pasajeros<contador):
            contador=i.pasajeros
    for a in l:
        if(a.pasajeros==contador):
            l.remove(a)
            
    return l


def mastripulacion(lista):
    contador=0
    l=[]
    for i in lista:
        if (i.tripulacion>contador):
            contador=i.tripulacion
    for a in lista:
        if(a.tripulacion==contador):
            l.append(a)
            
    return l


def AT(lista):
    l=[]
    for i in lista:
        if (i.nombre[0]=='A') and (i.nombre[1]=='T'):
            l.append(i)

    return l


def pasajeros6(lista):
    l=[]
    for i in lista:
        if(i.pasajeros>=6):
            l.append(i)
    
    return l


def naves(lista):
    l=[]
    contadorPeq=50000
    for i in lista:
        if(i.tripulacion<contadorPeq):
            contadorPeq=i.tripulacion
    contadorMay=0
    for i in lista:
        if(i.tripulacion>contadorMay):
            contadorMay=i.tripulacion
    for i in lista:
        if(i.tripulacion==contadorMay or i.tripulacion==contadorPeq):
            l.append(i)

    return l

    
















def main():
    #INFORMACIÓN ESTRELLA M Y HALCÓN
    a=EstrellaMuerte()
    b=HalconMilenario()
    c=ATAP()
    d=CañoneraLAAT()
    e=ATTE()
    lista=[a,b,c,d,e]
    a.__str__()
    b.__str__()
    lista=[a,b,c,d,e]
    listapasajeros=toppasajeros(lista)
    print("El top de las naves con mas pasajeros es:   ",listapasajeros)
    lista=[a,b,c,d,e]
    listatripulacion=mastripulacion(lista)
    print("La nave con mas tripulacion es:  ",listatripulacion)
    lista=[a,b,c,d,e]
    NombreAT=AT(lista)
    print("Las naves que empiezan por AT son:    ",NombreAT)
    Pasajeros6=pasajeros6(lista)
    print("Las naves con mas de 6 pasajeros son:   ",Pasajeros6)
    navess=naves(lista)
    print("La nave mas grande y mas pequeña son:  ",navess)







    







if __name__=='__main__':
    main()