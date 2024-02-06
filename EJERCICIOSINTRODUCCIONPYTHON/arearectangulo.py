'''
Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.
'''
def area_rectangulo(b,h):
  area = b * h
  return area
longitud = float(input("Introduce la longitud del rectángulo: "))
ancho = float(input("Introduce el ancho del rectángulo: "))
print("El área del rectángulo es:", area_rectangulo(longitud,ancho))