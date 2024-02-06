'''
 Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.
 '''
def par_impar(numero) :
  if numero % 2 == 0 :
    print("El número es par")
  else :
    print("El número es impar")
num = int(input("Ingresa un número: "))
par_impar(num)