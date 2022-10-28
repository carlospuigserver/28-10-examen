from pilas import *

torre1=Pila()
torreaux=Pila()
torre2=Pila()

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
       print(princip-1,"---",final-1)
    else:
        hanoi(n-1,princip,aux,final) 
        print(princip-1,"---",final-1)
        hanoi(n-1,aux,final,princip)  
        
def llenar(n):
    for i in range(n, -1,-1):
        torre1[0].apilar(i)
        torreaux[1].apilar(0)
        torre2[2].apilar(0)
        
    torre1[0].puntero=n
    torreaux[1].puntero=0
    torre2[2].puntero=0
    

    o=int(input("La cantidad de discos es:"))

    hanoi(n,1,2,3)
    llenar(n)


