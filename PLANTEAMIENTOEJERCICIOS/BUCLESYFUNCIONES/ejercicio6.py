'''
 Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.
'''
def mcm(a,b) :
  if a == 0 or b==0 :
    return 0
  else :
    mayor = max(a,b)
    while True :
      if (mayor % a == 0) and (mayor % b == 0) :
        return mayor
      mayor += 1
n1 = int(input("Ingresa un número: "))
n2 = int(input("Ingresa un número: "))
print("El MCM de", n1,"y", n2, "es:", mcm(n1,n2))