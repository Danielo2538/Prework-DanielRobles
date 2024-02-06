# Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.
def valor_absoluto(lista) :
  for numero in range(len(lista)) :
   lista[numero] = abs(lista[numero])
  return lista
numeros = [0,7,-3,12,-12,-4,0]
print("Valores absolutos:", valor_absoluto(numeros))