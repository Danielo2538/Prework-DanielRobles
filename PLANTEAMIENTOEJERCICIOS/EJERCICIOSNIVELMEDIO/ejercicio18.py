'''
Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
'''
def segundo_mayor(lista) :
  lista.sort() #ordena la lista
  lista.pop() #elimina el último elemento de la lista
  maximo = 0
  for number in lista :
    if number > maximo:
      maximo = number
  return maximo
l = [3,6,1,12,8,5,6,4,9,1]
print("El 2º número mayor es:", segundo_mayor(l))