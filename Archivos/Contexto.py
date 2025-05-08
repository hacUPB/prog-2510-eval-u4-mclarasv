# Solicitamos al usuario el nombre del archivo a crear
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
nombre_archivo += ".txt"
print(nombre_archivo)
# Usamos 'with' para crear el contexto y escribir datos en el archivo 
with open(nombre_archivo, 'w') as archivo:
    # Solicitamos al usuario los datos a escribir en el archivo
    datos = (input("Ingrese su nombre: "))

    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("tipo de datos equivocados")
    archivo.write(datos)
    archivo.write("\n")
    archivo.write(str(edad))
    
# Ahora usamos 'with' para crear el contexto donde leer los datos del archivo
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

