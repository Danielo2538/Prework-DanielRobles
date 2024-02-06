# Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.
def signo_numero(numero) :
  if numero > 0 :
    return "positivo."
  elif numero < 0 :
    return "negativo."
  else :
    return "cero."
n = int(input("Ingresa un número: "))
print("El número", n, "es", signo_numero(n))