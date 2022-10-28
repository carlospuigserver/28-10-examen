matriz=[
    [0,3,4],
    [1,5,6],
    [2,7,9]
]

print(len(matriz))

def sarrus (matriz):
    resultado=0
    for i in range(3):
        resultado= ((matriz[0][0] * matriz[1][1] * matriz[2][2])+(matriz[1][0] * matriz[2][1]*matriz[0][2]) +(matriz[0][1] * matriz[1][2] * matriz[2][0]))-(matriz[0][2] * matriz[1][1] * matriz[2][0] )-(matriz[0][1]*matriz[1][0]*matriz[2][2])-(matriz[1][2] * matriz[2][1] * matriz[0][0])
    return resultado

print("El resultado del determinante es:   ",sarrus(matriz))