'''
Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas.
'''
def norepiten_listas(l1,l2) :
  nueva = []
  for i in l1 : # recorre la lista 1 
    if i not in nueva and i not in l2 : # busca los elentos que no están en la lista 2
      nueva.append(i) # añade elementos a la lista nueva
  for i in l2 : # recorre la lista 2
    if i not in nueva and i not in l1 : # busca los elementos que no están en la lista 1
      nueva.append(i) # añade más elelmentos a la lista nueva
  return nueva # devuelve la lista nueva
print("Elementos comunes a las 2 listas:", norepiten_listas([1,2,3,4,5], [3,4,5,6,7,8]))