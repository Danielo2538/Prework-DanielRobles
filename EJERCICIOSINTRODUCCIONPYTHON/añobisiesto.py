'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
'''
def año_bisiesto(año) :
  if año % 4 == 0 :
    return 'bisiesto.'
  else :
    return 'no es bisiesto.'
y = int(input('Introduce un año: '))
print('El año', y,'es', año_bisiesto(y))