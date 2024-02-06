'''
 Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.
'''
def cad_inv(lista) :
  cadena_invertida = cadena[: : -1]
  return(cadena_invertida)
cadena = input("Introduce una cadena:")
print("La cadena invertida es:", cad_inv(cadena))