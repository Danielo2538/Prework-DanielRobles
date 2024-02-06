'''
 Define una función que encuentre el elemento más común en una lista.
'''
def mas_repetido(lista):
  return max(set(lista), key = lista.count)
l=[2,3,4,2,5,6,7,2,4,2,9,1]
print(mas_repetido(l))