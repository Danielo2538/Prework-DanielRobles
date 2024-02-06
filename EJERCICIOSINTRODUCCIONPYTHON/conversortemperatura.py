'''
Conversor de Temperatura:
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''
def celsius_farenheit(numero) :
  farenheit = numero * 1.8 + 32
  return farenheit
celsius = int(input("Introduce temperatura en ºC:"))
print(celsius, "ºC son:", celsius_farenheit(celsius), "ºF.")