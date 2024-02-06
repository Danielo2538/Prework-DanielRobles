'''
 Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False
'''
def primo(numero) :
  for n in range(2, numero) :
    if numero % n == 0 :
      print("El número no es primo")
      return False
  print("El número es primo")
  return True
x = int(input("Ingresa un número: "))
primo(x)