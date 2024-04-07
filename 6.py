def adivinar_numero():

  minimo = 1
  maximo = 100

  while minimo <= maximo:
    mitad = (minimo + maximo) // 2

    respuesta = input(f"El número secreto está en la mitad inferior del rango actual ({minimo}-{mitad})? (Sí/No) ").lower()

    if respuesta == "sí":
      maximo = mitad - 1

    elif respuesta == "no":
      minimo = mitad + 1

  return minimo

numero_secreto = adivinar_numero()

print(f"¡Felicidades! Adivinaste el número secreto: {numero_secreto}")