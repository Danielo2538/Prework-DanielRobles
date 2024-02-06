'''
 Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
'''
def orden_inverso(lista) :
  lista.reverse()
  print(lista)
l = [3,6,1,2,8,5,6,4,9,1]
print("La lista en orden inverso:")
orden_inverso(l)