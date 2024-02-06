'''
 Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
'''
def elemento_comun(l1,l2) :
  nueva = []
  for i in l1 :
    if i not in nueva and i in l2 :
      nueva.append(i)
  if len(nueva) == 0:
    return False
  else :
    return True
print(elemento_comun([1,2,3,4,5], [5,6,7,8]))