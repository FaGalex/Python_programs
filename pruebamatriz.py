
from calendar import different_locale


def diagonalDifference(arr):
    # Write your code here
    lista = len(arr)
    diagonal=0
    diagonal2=0
    
    for i in range(lista):
        # print(arr[i])
        newlista=arr[i]
        lista2 = len(newlista)
        for j in range (lista2):
            # print (newlista[j]) 
            if (i==j):
                #print(newlista[j]) 
                numero=newlista[j]
                diagonal=numero+diagonal

    j=0
    
    for i in range(lista):
        # print(arr[i])
        newlista=arr[i]
        lista2 = len(newlista)
        newlista = newlista[::-1]
        print(newlista)
        for j in range (lista2):
            if (i==j):
                #print(newlista[j]) 
                numero=newlista[j]
                diagonal2=numero+diagonal2

    if (diagonal>diagonal2):
        diferencia = diagonal-diagonal2
    else:
        diferencia = diagonal2-diagonal

    return diferencia
         

arr = [ [ 11, 2, 4 ], [ 4, 5, 6 ], [ 10, 8, -12 ]]    
print(diagonalDifference(arr))

