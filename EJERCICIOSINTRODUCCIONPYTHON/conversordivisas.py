'''
Conversor de Divisas
Ejercicios Introducción a Python: Enunciados 2
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''
def conversor_divisas(d):
  e = 0.85 * d
  print(d, "$ son:", e, "€.")
n = float(input("Introduce la cantidad de dolares:"))
conversor_divisas(n)