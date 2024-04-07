def calcular_divisores(numero):

  divisores = []
  for i in range(1, numero + 1):
    if numero % i == 0:
      divisores.append(i)

  return divisores

numero = int(input("Introduzca un número entre 2 y 50: "))

divisores = calcular_divisores(numero)

print(f"Los divisores de {numero} son: {divisores}")