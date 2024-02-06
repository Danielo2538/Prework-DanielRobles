'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario
'''
def suma_lista(lista):
  suma = 0
  for i in lista:
    suma += i
  return suma
l = [1,4,-2,5,10]
print('La suma de los números es:', suma_lista(l))