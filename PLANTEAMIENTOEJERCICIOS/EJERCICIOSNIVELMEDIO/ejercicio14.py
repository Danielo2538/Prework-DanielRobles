'''
 Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
'''
def palabras_largas(lista,n) :
  largas = []
  cont = 0
  for i in lista:
    if len(i) > n:
      largas.append(i)
  return largas
         

l = ['casa','puerta','tejado', 'picaporte','linterna','mesa']
num = int(input("Introduce un número:"))
print("las palabras más largas que", num, "son:", palabras_largas(l,num))