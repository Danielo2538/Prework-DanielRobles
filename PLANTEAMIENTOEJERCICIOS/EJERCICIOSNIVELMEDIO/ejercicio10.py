'''
 Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
 '''
def interseccion_listas(l1,l2) :
  nueva = []
  for i in l1 :
    if i not in nueva and i in l2 :
      nueva.append(i)
  return nueva
print("Elementos comunes a las 2 listas:", interseccion_listas([1,2,3,4,5], [3,4,5,6,7,8]))