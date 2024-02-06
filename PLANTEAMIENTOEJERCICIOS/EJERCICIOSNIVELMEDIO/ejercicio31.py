'''
: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos.
'''
def primo(numero) :
  for n in range(2, numero) :
    if numero % n == 0 :
      #print("El número no es primo")
      return False
  #print("El número es primo")
  return True
x = int(input("Ingresa un número: "))

print("Los números primos hasta", x, "son:")

cont = 0
for i in range(2, x+1):
  if primo(i) == True :
    cont += 1
    print(i)
print("El total de primos es:", cont)