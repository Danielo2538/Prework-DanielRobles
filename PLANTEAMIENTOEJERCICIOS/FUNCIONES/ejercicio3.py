# Define una función que tome un número y determine si es primo. 
def primo(numero) :
  for n in range(2, numero):
    if numero % n ==0 :
      print("El número no es primo.")
      return False
  print("El número es primo.")
  return True
primo(121)