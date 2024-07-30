# EXAMEN UNIDAD 2 DE LA ESIT - FUNDAMENTOS DE PROGRAMACION CON PYTHON
# EJERCICIO #1
# Se estan evaluando cadenas, subcadenas, funciones, operadores

largo = 198.90
ancho = 67.57

def calcular_perimetro(largo, ancho):
    return (largo*2) + (ancho*2)

# print(calcular_perimetro(largo, ancho))


# EJERCICIO #2

"""
Escribe un programa que solicite al usuario su peso en kilogramos y su altura en metros, y luego 
calcule y muestre su índice de masa corporal (IMC). La fórmula para calcular el IMC es: 
IMC = peso entre altura al cuadrado.

Si el usuario ingresa el valor del peso 89.67 kilogramos y el valor de la altura 1.78 metros 
¿cuánto es el valor del IMC?
"""

peso = 89.67
altura = 1.78

def calcular_IMC(peso, altura):
    return (peso/altura**2)

print(calcular_IMC(peso, altura))