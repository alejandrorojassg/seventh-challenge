def es_primo(numero):
  
  if numero <= 1:
    return False

  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False

  return True

def imprimir_primos(n):
  
  print("Números primos del 1 al", n)
  for i in range(2, n + 1):
    if es_primo(i):
      print(i)

imprimir_primos(100)