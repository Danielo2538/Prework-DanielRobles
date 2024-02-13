'''
CALCULADORA: EJERCICIO PRÁCTICOM 1 EN PYTHON:
Necesitamos crear una calculadora funcional la cual nos permita introducir dos 
números por pantalla y devolvernos el resultado de una operación automáticamente, 
solo seleccionando la operación que deseamos realizar sobre lo números. 
Esta calculadora debe poder hacer las operaciones básicas, así 
como raíces cuadradas y potencias. 
'''

def sumar(a,b):
  return a + b

def restar(a,b):
  return a - b

def multiplicar(a,b):
  return a * b

def dividir(a,b):
  #if b != 0:
  return a / b
  #else:
    #print('No se puede dividir un número entre 0.')

def cuadrado(a):
  return a * a

def potencia(a,b):
  return a ** b

def raiz_cuadrada(a):
  if a >= 0:
    raiz = 0
    for i in range(int(a)):
      raiz = i * i
      if raiz == a:
        return i
  else:
    return 'ERROR'

def porcentaje(a,b):
  return a * (b/100)

def calculadora():
  print('Bienvenido a la calculadora')
  while True :
    operacion = input('Introduce la operación que quieres realizar: sumar/restar/multiplicar/dividir/cuadrado/potencia/raiz/porcentaje, o s para salir: ')

    if operacion == 'sumar':
      x = float(input('Introduce primer número: '))
      y = float(input('Introduce segundo número: '))
      print('La suma de los números', x,'e', y,'es', sumar(x,y))

    elif operacion == 'restar':
      x = float(input('Introduce primer número: '))
      y = float(input('Introduce segundo número: '))
      print('La resta de los números', x,'e', y,'es', restar(x,y))

    elif operacion == 'multiplicar':
      x = float(input('Introduce primer número: '))
      y = float(input('Introduce segundo número: '))
      print('La multiplicación de los números', x,'e', y,'es', multiplicar(x,y))

    elif operacion == 'dividir':
      x = float(input('Introduce dividendo: '))
      y = float(input('Introduce divisor: '))
      if y != 0:
        print('La división de los números', x,'e', y,'es', dividir(x,y))
      else:
        print('No se puede dividir un número entre 0.')

    elif operacion == 'cuadrado':
      x = float(input('Introduce número: '))
      print('El cuadrado de:', x, 'es', cuadrado(x))

    elif operacion == 'potencia':
      x = float(input('Introduce la base: '))
      y = float(input('Introduce la potencia: '))
      print('El número', x,'elevado a', y,'es', potencia(x,y))

    elif operacion == 'raiz':
      x = float(input('Introduce un número: '))
      print('La raiz cuadrada de', x,'es', raiz_cuadrada(x))

    elif operacion == 'porcentaje':
      x = float(input('Introduce un número: '))
      y = float(input('Introduce el porcentaje a calcular: '))
      print('El', y,'de', x,'es', porcentaje(x,y))

    elif operacion == 's':
      break
    
    else: 
      print('Valor introducido incorrecto.')

calculadora()