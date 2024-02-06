'''
Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def palindromo(p):
  if p == p [::-1]:
    print("La palabra es un palindromo.")
  else :
    print("La palabra no es un palindromo.")
palabra = input("Introduce una palabra:")
palindromo(palabra)