# -*- coding: utf-8 -*-
"""

Programa para obtener algoritmo minimo para torre de Hanoi usando recursividad

CLUB ALGORITMIA UPIITA

Aaron Merlos

"""

def Hanoi(discos, origen, destino, auxiliar):
    if (discos==1):
        print("Mueve el disco 1 del poste {}  al poste {}".format(origen, destino))
        return
    
    Hanoi(discos-1, origen, auxiliar, destino)
    print("Mueve el disco {} del poste {}  al poste {}".format(discos,origen,destino))
    Hanoi(discos-1, auxiliar, destino, origen)
    
    
if  __name__ ==  '__main__':
    print("\t***ALGORITMO MINIMO TORRE DE HANOI***")
    print("\n\nPara el algoritmo se usara la siguiente nomenclatura:\n\tPoste de origen = 'A'\n\tPoste auxiliar = 'B'\n\tPoste de destino = 'C'")
    discos = input("\nIntroduzca el numero de discos de su torre de Hanoi: ")
    discos=int(discos)
    print("\n\n\tEl algoritmo minimo para {} discos es el siguiente: \n".format(discos))
    Hanoi(discos, 'A', 'B', 'C')
    