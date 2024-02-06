'''
Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
PISTA: Para convertir un número a string usa el método str(). Te recordamos que para saber la longitud de una cadena utilizamos len()
'''
def cantidad_digitos(numero) :
  longitud = len(str(numero))
  return longitud
n = int(input("Ingresa un número: "))
print("La cantidad de digitos es:", cantidad_digitos(n))