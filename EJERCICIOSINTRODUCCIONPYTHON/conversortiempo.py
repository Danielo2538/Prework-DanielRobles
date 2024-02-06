'''
: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''
def conversor_minutos(m):
  horas = m // 60
  minutos = m % 60 
  print(horas, 'horas')
  print(minutos, 'minutos')
x = int(input('Introduce la cantidad de minutos a convertir: '))
print(x, 'minutos son:')
conversor_minutos(x)