'''
Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''
def num_primo(numero) :
  if numero % 2 == 0:
    #return False
    print("El número introducido no es primo.")
  else :
    #return True
    print("El número introducido es primo.")
n = int(input("Introduce un número: "))
num_primo(n)