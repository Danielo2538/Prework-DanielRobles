#  Defineuna función que tome un número y retorne su factorial. 
def factorial() :
  n = 9
  cont = 0
  total = 1
  while cont < n :
    cont +=1
    total *= cont
  print(total)
factorial()