# Define una función que reciba una cadena de texto y retorne la cadena en reversa. 
def cad_inv(lista) :
  cadena_invertida = cadena[: : -1]
  #print(cadena_invertida)
  return(cadena_invertida)
cadena = "hola mundo"
#cad_inv(cadena)
print(cad_inv(cadena))