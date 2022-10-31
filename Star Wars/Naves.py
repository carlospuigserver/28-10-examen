class Nave:
    def __init__(self,nombre,longitud,tripulacion,pasajeros):
        self.nombre=nombre
        self.longitud=longitud
        self.tripulacion=tripulacion
        self.pasajeros=pasajeros

class EstrellaMuerte(Nave):
    def __init__(self):
        self.nombre="Estrella de la Muerte"
        self.longitud=120000
        self.tripulacion=1350000
        self.pasajeros=1500000

    def __str__(self):
        print("Toda la información de la Estrella de la muerte es: \n")
        f'Longitud =   {self.longitud} metros \n'
        f'Tripulación =   {self.tripulacion} personas \n'
        f'Pasajeros =   {self.pasajeros} personas \n'


class HalconMilenario(Nave):
    def __init__(self):
        self.nombre="Halcón Milenario"
        self.longitud=34
        self.tripulacion=4
        self.pasajeros=10
    
    def __str__(self):
        print("Toda la información del Halcón Milenario es: \n")
        f'Longitud =   {self.longitud} metros \n'
        f'Tripulación =   {self.tripulacion} personas \n'
        f'Pasajeros =   {self.pasajeros} personas \n'

class ATAP(Nave):
    def __init__(self):
        self.nombre="AT-AP"
        self.longitud=25
        self.tripulacion=3
        self.pasajeros=13

class CañoneraLAAT(Nave):
    def __init__(self):
        self.nombre="Cañonera LAAT"
        self.longitud=17
        self.tripulacion=4
        self.pasajeros=30
