'''
Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''
def calculadora_simple(a,b,operador):
  resultado = 0
  if operador == '+' :
    resultado = a + b
  elif operador == '-' :
    resultado = a - b
  elif operador == '*' :
    resultado = a * b
  elif operador == '/' :
    resultado = a / b
  else :
    resultado = 'operador erroneo'
  return resultado
n1 = int(input("Introduce número 1:"))
n2 = int(input("Introduce  número 2:"))
op = input("Introduce operación a realizar (+,-,*,/):")
print("El resultado es:", calculadora_simple(n1,n2,op))