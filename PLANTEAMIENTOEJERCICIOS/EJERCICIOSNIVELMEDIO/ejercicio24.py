'''
 Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
'''
def tabla_numero(n) :
  for i in range(1, 11):
    print(f'{i} x {n} = {i * n}')
numero = int(input("Introduce un número:"))
tabla_numero(numero)