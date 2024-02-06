'''
Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original. 
'''
def unicos(lista) :
  lista_unicos = list(set(lista))
  print(lista_unicos)
numeros = [1,2,2,3,4,4,5,7,7,8]
unicos(numeros)