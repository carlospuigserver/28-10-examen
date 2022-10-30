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




#Funciones

def agregar_termino(polinomio, termino, valor):
    
    aux = Nodo()
    dato = datoPolinomio(valor,termino)
    aux.info = dato
    if (termino > polinomio.grado):
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        actual = polinomio.termino_mayor
        while(actual.sig is not None and termino < actual.sig.info.termino):
            actual = actual.sig
        aux.sig = actual.sig
        actual.sig = aux




def modificar(polinomio, termino, valor):
    aux = polinomio.termino_mayor
    while (aux is not None and aux.info.termino != termino):
        aux = aux.sig
    aux.info.valor = valor



#RESTA
def resta(polinomio1, polinomio2):
   
    paux = Polinomio()
    mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
    for i in range(0, mayor.grado +1):
        total = determinar_valor(polinomio1, i) - object(polinomio2, i)
        if (total != 0):
            agregar_termino(paux, i, total)
    return paux



#DIVISIÓN
def dividir(polinomio1, polinomio2):
    
    paux = Polinomio()
    pol1 = polinomio1.termino_mayor
    while (pol1 is not None):
        pol2 = polinomio2.termino_mayor
        while (pol2 is not None):
            termino = pol1.info.termino - pol2.info.termino
            valor = pol1.info.valor // pol2.info.valor
            if (determinar_valor(paux, termino) != 0):
                valor += determinar_valor(paux, termino)
                modificar(paux, termino, valor)
            else:
                agregar_termino(paux, termino, valor)
            pol2 = pol2.sig
        pol1 = pol1.sig
    return 




#DETERMINAR VALOR
def determinar_valor(polinomio, termino):
   
    aux = polinomio.termino_mayor
    while(aux is not None and aux.info.termino != termino):
        aux = aux.sig
    if (aux is not None and aux.info.termino == termino):
        return aux.info.valor
    else:
        return 0



#ELIMINAR VALOR
def eliminar_valor(polinomio,termino):
    pol1=polinomio.termino_mayor
    while pol1 is not None:
        Terpol1=pol1.info.termino
        if Terpol1==termino:
            pol1.info.valor=0
            break
        else:
            pol1=pol1.sig






