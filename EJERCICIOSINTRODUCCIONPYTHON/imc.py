'''
Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
def masa_corporal(peso,altura):
  imc = peso / altura**2
  print("El IMC de", n, "es:", imc)
p = float(input("Introduce el peso en Kg:"))
h = float(input("Introduce la altura en metros:"))
n = input("Introduce nombre del paciente:")
masa_corporal(p,h)