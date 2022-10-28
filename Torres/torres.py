from pilas import *

def crearDis(n):
    torre = [[]]
    copiar=n
    
    for i in range(2*n+3):  
        if i==(2*n+3)//2:
            torre[0].append("i")
        else:
            torre[0].append(" ")
            
            
    for i in range(1,n+1):
        torre.append([])
        for j in range(2*n+3):
            if j < copiar -1 or j> (2*i+copiar+1):
                torre[i].append(" ")
                
            elif j==copiar-1:
                torre[i].append("[") 
            elif j==(2*i+copiar+1):
                torre[i].append("]")
            else:
                torre[i].append("=")
                
        copiar-=1
        

    
    
def hanoi(n,princip,final,aux):
    if n == 1:
        movimiento(princip-1,"---",final-1)
    else:
        hanoi(n-1,princip,aux,final) 
        movimiento(princip-1,"---",final-1)
        hanoi(n-1,aux,final,princip)  
        
def llenar(n):
    for i in range(n, -1,-1):
        pilas[0].apilar(i)
        pilas[1].apilar(0)
        pilas[2].apilar(0)
        
    pilas[0].puntero=n
    pilas[1].puntero=0
    pilas[2].puntero=0
    
def movimiento(origen,destino):
    pintar()
    dato=pilas[origen].desapilar()
    pilas[destino].apilar(dato)
    print(1)
   
    
def pintar(n):
    
    for i in range(n,-1,-1):
        for j in range(3):
            dibujar_discos(pilas[j].items[i])
        print()

def dibujar_discos(noDiscos):
    for i in torre[noDiscos]:
        print(i,end="")
        
def llenar_pilas(n):
    for i in range(n,-1,-1):

O=int(input("Esta es la cantidad de discos:"))
torre=crearDis
pilas = [Pila(),Pila(),Pila()]
llenar_pilas
hanoi(1,2,3,O)
pintar()
