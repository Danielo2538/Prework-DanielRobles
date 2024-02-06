'''
Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena.
'''
def apariciones_caracter(cadena) :
  diccionario = {} # variable diccionario
  for i  in cadena : #recorre la cadena
    if i in diccionario :# si encuentra el caracter en el diccionario
      diccionario[i]+=1# sumaa una vez por cada vez que el caracter aparece
    else:
      diccionario[i]=1 #si el caracter no se repite solo queda en 1
  for caracter, valor in diccionario.items(): # añade valores al diccionario
    print(caracter, "se repite", valor, "veces.")
cad = input("Introduce una cadena:")
apariciones_caracter(cad)