# Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
def contar_letras(palabra) :
  return(len(palabra))
p = input("Ingresa una palabra: ")
print("La cantidad de letras de la palabra", p, "es:", contar_letras(p))