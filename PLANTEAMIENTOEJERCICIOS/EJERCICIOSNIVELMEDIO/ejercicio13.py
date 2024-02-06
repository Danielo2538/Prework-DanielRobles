'''
Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
'''
def orden_ascendente(lista) :
  lista.sort()
  print(lista)
l = [3,6,1,2,8,5,6,4,9,1]
print("La lista en orden ascendente:")
orden_ascendente(l)