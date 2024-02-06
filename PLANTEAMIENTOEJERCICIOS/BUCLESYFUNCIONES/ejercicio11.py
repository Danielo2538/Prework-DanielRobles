# Crea una función que, dado un número, verifique si un número es primo.
def primo(numero) :
  for n in range(2, numero) :
    if numero % n == 0 :
      print("El número no es primo")
      return False
  print("El número es primo")
  return True
x = int(input("Ingresa un número: "))
primo(x)