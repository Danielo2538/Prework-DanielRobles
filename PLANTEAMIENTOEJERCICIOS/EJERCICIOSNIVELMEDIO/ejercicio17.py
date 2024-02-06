'''
 Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
'''
def sumar_cubo(numero):
  suma = 0
  while numero > 0 :
    suma =suma + (numero%10)**3
    numero = numero//10
  print(suma)
n = int(input("Ingresa un número:"))
print("La suma de los digitos en potencia 3 es:")
sumar_cubo(n)