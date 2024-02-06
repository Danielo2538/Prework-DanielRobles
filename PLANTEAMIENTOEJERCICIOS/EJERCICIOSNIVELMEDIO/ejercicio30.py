'''
Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista.
'''
def cadena_larga(lista) :
  longitud=[]
  for i in lista :
    longitud.append((i, len(i))) #añade una tupla con la cadena y su longitud
  longitud.sort() #ordena la lista de mayor a menor en forma de tupla
  return longitud[0][0] # devuelve el primer elemento de la lista y el primer elemento de la tupla,es decir la cadena más larga
l = ['uno', 'dos', 'cuarenta', 'tres']
print("La cadena más larga es:", cadena_larga(l))