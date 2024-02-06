# Define una función que reciba una lista de números y retorne la suma de ellos. 
def suma_num(numeros) :
  suma = 0
  for n in numeros :
    suma += n
  print(suma)
lista = [1,2,2,4,78]
suma_num(lista)