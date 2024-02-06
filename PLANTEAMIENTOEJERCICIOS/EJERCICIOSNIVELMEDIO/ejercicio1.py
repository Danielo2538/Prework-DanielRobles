'''
Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci. 
'''
def fibonacci(numero) :
  cont = 0
  total = 1
  for num in range(numero) :
    temp = cont + total
    cont = total
    total = temp
  return total
n = int(input("Ingresa un número:"))
print("Los", n, "primeros números de la serie de Fibonacci son:")
print(0)
for x in range(n - 1) :
  print(fibonacci(x))