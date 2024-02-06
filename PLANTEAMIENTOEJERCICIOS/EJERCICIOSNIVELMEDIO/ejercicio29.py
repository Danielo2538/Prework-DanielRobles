'''
Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.
'''
def promedio(lista) :
  suma = 0
  cont = 0
  for i in lista :
    cont += 1
    suma += i
  return suma / cont
l = [2,3,2,3,4,4]
print("El promedio es:", promedio(l))