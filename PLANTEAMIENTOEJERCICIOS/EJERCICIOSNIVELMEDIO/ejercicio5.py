# Define una función que tome una cadena y cuente el número de vocales en la cadena. 
def contar_vocales(palabra) :
  vocales = "aeiouAEIOU"
  cont = 0
  for letra in palabra :
    if letra in vocales:
      cont +=1
  print(cont)
p = input("Ingresa un texto: ")
print("La cantidad de vocales de la cadena:", p, "es:") 
contar_vocales(p)