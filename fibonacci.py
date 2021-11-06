# -*- coding: utf-8 -*-
"""

Programa para obtener serie Fibonacci usando recursividad

CLUB ALGORITMIA UPIITA

Aaron Merlos

"""

def fibonacci(posicion):
    if posicion==0:
        return 0
    elif posicion==1:
        return 1
    return fibonacci(posicion-1)+fibonacci(posicion-2)



if  __name__ ==  '__main__':
    
   print("\t**PROGRAMA SERIE DE FIBONACCI USANDO RECURSIVIDAD***\n\n")
   
   pos=input("Introduzca el numero de la posicion que busca obtener de la serie Fibonacci: ")
   pos=int(pos)
   print("\n\nEl valor de la serie Fibonacci para la posicion {} es: {}".format(pos, fibonacci(pos)))