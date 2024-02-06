'''
 Define una función que reciba una lista de números y retorne la suma acumulada de los números
'''
def suma_acumulada(lista) :
  cont = 0
  suma =[]
  for i in l:
    cont += i
    suma.append(cont) # append() añade un nuevo elemento al final de la lista
  return(suma)
l = [1,2,3,4]
print("La lista con la suma acumulada es:", suma_acumulada(l))