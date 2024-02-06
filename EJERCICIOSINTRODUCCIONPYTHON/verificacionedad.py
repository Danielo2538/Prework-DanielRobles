'''
Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.
'''
def mayor_edad(n) :
  if n >= 18 :
    #return True
    print("El usuario es mayor de edad.")
  else :
    #return False
    print("El usuario es menor de edad.")
edad = int(input("Introduce la edad:"))
mayor_edad(edad)