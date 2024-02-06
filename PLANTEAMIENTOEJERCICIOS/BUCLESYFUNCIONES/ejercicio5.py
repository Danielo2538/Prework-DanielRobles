# Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
def sumar_digitos(numero) :
  suma = 0
  for digito in str (numero) :
    suma += int(digito)
  return suma
n = int(input("Ingresa un número: "))
print("La suma de los digitos de", n,"es:", sumar_digitos(n))