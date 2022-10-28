class Nodo:
    def __init__(self,info):
        self.info=info
        self.sig=None

class Pila:
    def __init__(self):
        self.superior=None
        self.tama=0

def apilar(pila,dato):
    print("Añadiendo {} en la cima de la pila".format(dato))
    if pila.superior==None:
        pila.superior =Nodo(dato)
        return
    nuevo_nodo=Nodo(dato)
    nuevo_nodo.sig=pila.superior
    pila.superior=nuevo_nodo
    pila.tam +=1

def despilar(pila):
    if pila.superior==None:
        print("no hay ningun elemento")
        return
    print("despilar {}".format(pila.superior.info))
    pila.superior=pila.superior.sig
    pila.tama -=1

def imprimir(pila):
    print("Se imprime la pila:")
    nodo_temporal=pila.superior
    while nodo_temporal!= None:
        print("{}".format(nodo_temporal.info))
        nodo_temporal=nodo_temporal.sig
    print("")

def pila_vacia(pila):
    return pila.superior is None

def encima(pila):
    if pila.superior is not None:
        return pila.superior.info
    else:
        return None

def tama(pila):
    return pila.tama