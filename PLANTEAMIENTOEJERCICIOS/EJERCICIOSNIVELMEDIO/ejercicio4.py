# Define una función que tome un número y retorne la suma de sus dígitos. 
def sumar_digitos(numero) :
  suma = 0
  for digito in str (numero) :
    suma += int(digito)
  return suma
n = int(input("Ingresa un número: "))
print("La suma de los digitos de", n,"es:", sumar_digitos(n))