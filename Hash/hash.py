def bernstein(string):
    a=0
    for caracter in string:
        a=a*33 +ord(caracter)
    
    return a


class tablaHash():
    def __init__(self,tama):
        self.tama=tama
        self.tabla=[None]*tama
        self.key

    def funcionHash(self,dato):
        return bernstein(dato)%self.tama


    def insert(self,dato):
        ubicacion=self.funcionHash(dato)
        if (self.tabla[ubicacion] is None):
            self.tabla[ubicacion]=dato
        else:
            print("Ha colisionado")

        tabl=tablaHash()
        print(tabl.tabla)
        tabl.insert("")
        print(tabl.tabla)
        tabl.insert("")

    