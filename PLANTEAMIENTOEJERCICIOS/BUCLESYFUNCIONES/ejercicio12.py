'''
Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.
'''
def mcd(a,b) :
  while b :
    a,b = b,a % b
  return a
n1 = int(input("Ingresa número 1: "))
n2 = int(input("Ingresa número 2: "))
print("El máximo común divisor es:",mcd(n1,n2))