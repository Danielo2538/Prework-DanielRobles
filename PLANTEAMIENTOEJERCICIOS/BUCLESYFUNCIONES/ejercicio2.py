'''
Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.
'''
def factorial(numeros) :
  cont = 0
  total = 1
  while cont < numeros :
    cont += 1
    total *= cont
  return total
n = int(input("Ingresa un número: "))
print("El factorial de", n, "es:", factorial(n))