'''
Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
def suma_pares(cont):
  suma = 0
  cont = 0
  while cont <= 100:
    cont += 1
    if cont % 2 == 0 :
      suma += cont
  return suma
n = 100
print("La suma de los números pares del 1 al 100 es:", suma_pares(n))