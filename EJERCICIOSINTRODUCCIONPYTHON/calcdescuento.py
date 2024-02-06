'''
Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''
def calculadora_descuento(precio) :
  total = precio * 0.2
  return total
p = float(input("Introduce el precio del articulo: "))
print("El precio del articulo con el 20% de descuento es: ", calculadora_descuento(p), "€")