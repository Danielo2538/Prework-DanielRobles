'''
 Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.
'''
def contar_vocales(palabra) :
  vocales = "aeiouAEIOU"
  cont = 0
  for letra in palabra :
    if letra in vocales:
      cont +=1
  return cont
p = input("Ingresa un texto: ")
print("La cantidad de vocales de la cadena:", p, "es:") 
print(contar_vocales(p))