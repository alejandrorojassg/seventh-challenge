def calcular_year_superacion(poblacion_a, tasa_a, poblacion_b, tasa_b):

  year = 2022

  while poblacion_b <= poblacion_a:
    poblacion_a *= (1 + tasa_a)

    poblacion_b *= (1 + tasa_b)

    year += 1

  return year

poblacion_a = 25000000

tasa_a = 0.02

poblacion_b = 18900000

tasa_b = 0.03

year_superacion = calcular_year_superacion(poblacion_a, tasa_a, poblacion_b, tasa_b)

print(f"La población del país B superará a la del país A en el año {year_superacion}")