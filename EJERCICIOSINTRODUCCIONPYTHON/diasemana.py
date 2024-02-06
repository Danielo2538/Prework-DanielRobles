'''
Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''
def dia_semana(n) :
  dia = ['lunes','martes','miércoles','jueves','viernes','sábado','domingo']
  cont= 0
  for i in dia :
    cont += 1
    if cont == n:
      print(i)
numero = int(input("Introduce un número:"))
dia_semana(numero)