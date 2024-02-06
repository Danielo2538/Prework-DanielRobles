'''
: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
'''
def calculadora_edad(año) :
  actual = 2024
  edad = actual - año
  return edad
n = int(input("Introduce tu año de nacimiento:"))
print("Tienes", calculadora_edad(n), "años.")