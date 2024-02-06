# Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
def elementos_lista(lista, n) :
  print("Los", n,"primeors elementos de la lista son:")
  for numero in lista[0:n] :
    print(numero)
elementos_lista(['1','2','3','4','5'], 4)