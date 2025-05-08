frase = "hoy me dieron una cita medica"
palabras = frase.split()
print(palabras)
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)