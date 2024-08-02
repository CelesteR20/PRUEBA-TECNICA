
#EJERCICIO 1
from collections import Counter

def contar_unicos_repetidos(matriz):
    lista_plana = [numero for fila in matriz for numero in fila]
    conteo = Counter(lista_plana)
    
    unicos = sum(1 for vez in conteo.values() if vez == 1)
    repetidos = sum(1 for vez in conteo.values() if vez > 1)
    
    return [unicos, repetidos]

matriz1 = [[2, 2], [2, 2]]
matriz2 = [[2, 1, 3], [4, 5, 2], [6, 6, 6]]

print("Problema 1 :")
print(contar_unicos_repetidos(matriz1))
print(contar_unicos_repetidos(matriz2))



#EJERCICIO 2
def encontrar_pares_suma_n(n):
    pares = []
    vistos = set()
    
    for i in range(1, n):
        complemento = n - i
        if complemento > 0 and complemento not in vistos:
            pares.append((i, complemento))
            vistos.add(i)
    
    return pares

n = 10
print("Problema 2 :")
print(encontrar_pares_suma_n(n))