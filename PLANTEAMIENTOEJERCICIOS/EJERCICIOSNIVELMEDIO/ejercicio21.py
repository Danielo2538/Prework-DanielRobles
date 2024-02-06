'''
 Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
'''
def letras_digitos(cadena) :
  digitos = 0
  letras = 0
  for i in cadena:
    if i.isdigit() : #cuenta los números
      digitos += 1
    elif i.isalpha(): #cuenta las letras
      letras += 1
  #return digitos, letras
  print("La cantidad de digitos es:", digitos)
  print("La cantidad de letras es:", letras)
cad = input("introduce un texo:")
letras_digitos(cad)
