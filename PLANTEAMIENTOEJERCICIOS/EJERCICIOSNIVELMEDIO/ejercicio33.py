'''
: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.
'''
def orden_tuplas(lista) :
  #lista = [list(tupla) for tupla in lista ]
  #lista.sort(::-1)
  return (lista[1], -lista[1])
datos = [('uno',7), ('dos',5), ('cuarenta',23), ('tres',1)]
print(sorted(datos, key = orden_tuplas))