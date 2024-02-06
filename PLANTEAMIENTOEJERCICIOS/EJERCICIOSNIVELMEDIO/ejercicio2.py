'''
Define una función que tome un número y retorne una lista de sus divisores.
'''
def divisores(n) :
  cont = 0
  print("Los divisores de", n, "son:")
  if n == 0 :
    print(0)
  else :
    for div in range(1, n + 1) :
      if n % div == 0 :
        print(div) 
        cont += 1
num = int(input("Ingresa un número:"))
divisores(num)