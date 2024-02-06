'''
Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
'''
n = 0
cont = 0
while n < 50 :
  n +=1

  if (n % 3 != 0) and (n % 5 != 0):
    print(n)
    
  if (n % 3 == 0) and (n % 5 == 0):
    print("FizzBuzz")
  if n % 3 == 0:
    print("Fizz")
  if n % 5 == 0 :
    print("Buzz")