'''
Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''
def calculadora_propina(lista) :
  suma = 0
  total = 0
  for i in lista :
    suma += i
  total = suma + (suma * 0.15)
  return total
l = (12.3,13,15.8,3,2.5)
print("Total + propina:", calculadora_propina(l))