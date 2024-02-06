'''
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''
def contador_palabras(palabra):
  cont = 1
  espacio = ' '
  for i in palabra:
    if i == espacio:
      cont += 1
  return cont
p = input("Introduce una oración: ")
print("La oración contiene", contador_palabras(p), "palabras.")