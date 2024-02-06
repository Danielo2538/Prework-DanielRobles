# Define una función que reciba un número y retorne su representación en binario.
def binario_dec(numero):
  binario = ''
  while numero // 2 != 0 :
    binario = str(numero % 2) + binario
    numero = numero // 2
  return str(numero) + binario
n = int(input("Introduce un número:"))
print(binario_dec(n))