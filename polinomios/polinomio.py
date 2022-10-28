class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):
    

    def __init__(self,valor,termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):

    def __init__(self):
        self.termino_mayor = None
        self.grado = -1






#DETERMINAR VALOR
def determinar_valor(polinomio, termino):
   
    aux = polinomio.termino_mayor
    while(aux is not None and aux.info.termino != termino):
        aux = aux.sig
    if (aux is not None and aux.info.termino == termino):
        return aux.info.valor
    else:
        return 0





