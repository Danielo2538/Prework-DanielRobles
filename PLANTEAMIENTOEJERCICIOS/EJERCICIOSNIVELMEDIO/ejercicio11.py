'''
Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def palindromo(palabra):
  if str(palabra) == str(palabra) [::-1]:
    print("La palabra es un palindromo.")
  else :
    print("La palabra no es un palindromo.")
p = input("Introduce una palabra:")
palindromo(p)