'''
Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
'''
def mayusculas_minusculas(cadena) :
  cont = 0
  mayusculas = 0
  minusculas =0
  while cont < len(cadena) :
    letra = cadena[cont]
    if letra.isupper() == True :
      mayusculas += 1
    else :
      minusculas += 1
    cont += 1
  print("La cantidad de mayusculas es:", mayusculas)
  print("La cantidad de minusculas es:", minusculas)
string = input("Introduce una frase:")
mayusculas_minusculas(string)