# Dada una lista de números, crea una función que devuelva el número máximo de la lista.
def number_max(list) :
  maximo = 0
  for number in list :
    if number > maximo :
      maximo = number
  return maximo
numbers = [25,8,2,7,14]
print("El número máximo es:", number_max(numbers))