'''
Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
'''
def numero_perfecto(numero):
  suma = 0
  for i in range(1,numero):
    if numero % i == 0 : # if numero % (i) == 0 :
      suma += i # suma += (i)
  if numero == suma :
    return True
  else:
    return False
num = int(input("Introduzca un número: "))
if numero_perfecto(num):
  print("El número", num, "es perfecto.")
else :
  print("El número", num, "no es perfecto.")