'''
Define una función que tome una lista de números y retorne el número más grande de la lista.
'''
def mayor(list) :
  maximo = 0
  for number in list :
    if number > maximo :
      maximo = number
  return maximo
lista = [25,8,234,7,14,56,90]
print("El número mayor es:", mayor(lista))