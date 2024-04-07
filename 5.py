def calcular_factorial(n):

  if n == 0 or n == 1:
    return 1

  factorial = 1
  for i in range(2, n + 1):
    factorial *= i

  return factorial

n = int(input("Introduzca un número natural n: "))

factorial = calcular_factorial(n)

print(f"El factorial de {n} es {factorial}")