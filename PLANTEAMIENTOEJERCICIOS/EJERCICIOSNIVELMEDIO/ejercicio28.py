'''
Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número.
'''
def cuadrado_pares(n) :
  cont = 0
  suma = 0
  while cont < n :
    cont += 1
    if cont % 2 == 0:
      suma += cont ** 2
  return suma
num = int(input("Introduce un número:"))
print("La suma de los cuadrados de los pares hasta", num, "es:", cuadrado_pares(num))