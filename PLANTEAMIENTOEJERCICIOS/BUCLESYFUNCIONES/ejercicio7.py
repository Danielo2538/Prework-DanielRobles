'''
Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.
'''
def area_triangulo(b,h) :
  return b * h / 2
base = int(input("Ingresa la base del triangulo: "))
altura = int(input("Ingresa la altura del triangulo: "))
print("El área del triangulo es:", area_triangulo(base,altura))