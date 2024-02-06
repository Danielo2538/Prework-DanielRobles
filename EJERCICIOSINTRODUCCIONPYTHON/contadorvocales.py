'''
Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''
def contador_vocales(palabra):
  vocales= 'AEIOUaeiou'
  cont = 0
  for i in palabra :
    if i in vocales :
      cont +=1
  return cont
p = input("Introduce una palabra:")
print("La palabra", p,"tiene", contador_vocales(p), "vocales.")
