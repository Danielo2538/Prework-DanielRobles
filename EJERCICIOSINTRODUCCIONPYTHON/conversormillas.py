'''
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.
'''
def millas_km(milla):
  km = milla * 1.60934
  return km
m = float(input("Introduce distancia en millas: "))
print(m, "millas son:", millas_km(m), "kilometros.")