# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 08:26:43 2021

@author: DevSlein
"""
"""
if-else  (condicion o comparación o toma de decisión)

if condicion :
    codigo que se ejecuta si cumple la condicion
else:
    codigo que se ejecuta si no se cumple la condicion

"""
#%%
numero =10
if numero <=10:
    print(f"el valor es {numero}")
else:
    print("Es incorrecto")
#%%
"""
Bucles for
   Estructura de control que me permite iterar o repetir una operacion
   
   for variable in fuente_datos:
       codigo que se va a repetir
   
"""
datos = [1,2,3,4,5,6,7,8,9,10]
print(type(datos))
#for-each
for numero in datos:
    if numero %2 ==0:
        print(f"El {numero} es par")
    else :
        print(f"El {numero} es impar")
        
#Ejemplo1        
nombres="Carolina,Jesus,Veronica,Jorge,Erick"
listanombres = nombres.split(",") 
for nombre in listanombres:
    print(f"{nombre}")       
    
#Ejemplo2 mejorando el 1
for nombre in nombres.split(","):
    print(f"{nombre}")     
        
        
#forma simplificada
print("forma simplificada")
[numero for numero in datos if numero%2==0]        
print(numero)

#equivale a
for numero in datos :
    if numero%2 ==0:
        numero
#recorriendo un diccionario
"""
 Diccionar es una estructura de almacenamiento
      llave se le asocia un valor
      diccionario <clave, valor>
"""
dias_sem = { "Lunes":1, "Martes":2, "Miercoles": 3}

for llave in dias_sem:
    print(f"Dia {llave}")
    
#Recorrer con dia y clave
for llave, clave in dias_sem.items():
    print(f"El dia es: {llave} y la posicion es {clave}")
#%%
"""
bucles while
     estructura de control para iterar o repetir
     while condicion:
           lineas a ejecutar
           variable de incremento o decremenot
"""
i = 0
while i<=10:
    print(f"while {i}")
    i= i+1
    
#usando el input para solicitar datos
#valores = input("Ingresa un numero")
#print("El valor es {}".format(valores))
while 1:
    entrada = input("Ingresa un numero del 1 al 10 o 'exit'  ")
    try:
        if entrada == 'exit':
            print("salida")
            break
        elif int(entrada) <=10:
            cuadrado = int(entrada)**2
            print(f"El cuadrado {entrada} del numero es {cuadrado}")
        else:
            print("El valor no es valido")
    except ValueError:
        print("Error: no se puede convertir el numero {numero}".format(entradas))
#%%
"""
Uso try catch
"""
num_str = "10.5"
#vamos a intentar convertirlo
try:
    valor =int(num_str)
except Exception as e: #si falla por alguna causa continua con el flujo
    print("excepcion es: {} : {}".format(type(e),e))
    print("No se puede convertir el numero {}".format(num_str))    
