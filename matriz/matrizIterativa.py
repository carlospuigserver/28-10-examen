lista=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(len(lista))

def sarrus (lista):
    resultado=0
    for i in range(3):
        resultado= ((lista[0][0] * lista[1][1] * lista[2][2])+(lista[1][0] * lista[2][1]*lista[0][2]) +(lista[0][1] * lista[1][2] * lista[2][0]))-(lista[0][2] * lista[1][1] * lista[2][0] )-(lista[0][1]*lista[1][0]*lista[2][2])-(lista[1][2] * lista[2][1] * lista[0][0])
    return resultado

print(sarrus(lista))