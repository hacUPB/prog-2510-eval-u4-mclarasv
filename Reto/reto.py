import os
import csv
import matplotlib.pyplot as plt


def menu_principal():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Listar archivos")
    print("2. Procesar archivo de texto")
    print("3. Procesar archivo CSV")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def submenu_txt():
    print("\n====MENU .TXT====")
    print("1. Contar palabras y caracteres")
    print("2. Reemplazar palabra")
    print("3. Histograma de vocales")
    opcion_submenu1 = input("Seleccione una opción: ")
    return opcion_submenu1

def submenu_csv():
    print("\n====MENU .CSV====")
    print("1. Mostrar CSV")
    print("2. Estadísticas CSV")
    print("3. Graficar columna CSV")
    opcion_submenu2 = input("Seleccione una opción: ")
    return opcion_submenu2

def listar_archivos():
    ruta = input("Ingrese la ruta (deje vacío para usar la carpeta actual): ")
    if ruta.strip() == "":
        ruta = "."
    try:
        archivos = os.listdir(ruta)
        print("\nArchivos encontrados:")
        for archivo in archivos:
            print("-", archivo)
    except FileNotFoundError:
        print("Ruta no válida.")


def contar_txt():
    try:
        with open("ejemplo.txt", "r") as archivo:
            texto = archivo.read()
            palabras = texto.split()
            cantidad_palabras = len(palabras)
            cantidad_caracteres_con_espacios = len(texto)
            texto_sin_espacios = texto.replace(" ", "")
            cantidad_caracteres_sin_espacios = len(texto_sin_espacios)

            print("Cantidad de palabras:", cantidad_palabras)
            print("Cantidad de caracteres con espacios:", cantidad_caracteres_con_espacios)
            print("Cantidad de caracteres sin espacios:", cantidad_caracteres_sin_espacios)
    except FileNotFoundError:
        print("El archivo 'ejemplo.txt' no fue encontrado.")

def reemplazar_palabra():
    try:
        with open("ejemplo.txt", "r") as archivo:
            texto = archivo.read()

        palabra_a_reemplazar = input("Ingrese la palabra que desea reemplazar: ")
        palabra_nueva = input("Ingrese la nueva palabra: ")

        texto_modificado = texto.replace(palabra_a_reemplazar, palabra_nueva)

        with open("ejemplo.txt", "w") as archivo:
            archivo.write(texto_modificado)

        print("La palabra fue reemplazada correctamente.")
    except FileNotFoundError:
        print("El archivo 'ejemplo.txt' no fue encontrado.")


def histograma_vocales():
    try:
        with open("ejemplo.txt", "r") as archivo:
            texto = archivo.read()
            texto = texto.lower()

            cantidad_a = texto.count("a")
            cantidad_e = texto.count("e")
            cantidad_i = texto.count("i")
            cantidad_o = texto.count("o")
            cantidad_u = texto.count("u")

            vocales = ["a", "e", "i", "o", "u"]
            cantidades = [cantidad_a, cantidad_e, cantidad_i, cantidad_o, cantidad_u]

            #grafica
            plt.bar(vocales, cantidades, color="skyblue")
            plt.title("Histograma de vocales")
            plt.xlabel("Vocal")
            plt.ylabel("Cantidad")
            plt.show()
    except FileNotFoundError:
        print("El archivo 'ejemplo.txt' no fue encontrado.")



def mostrar_csv():
    archivo = "eventos_salud_publica.csv"
    try:
        with open(archivo) as f:      #guardamos esto en la variable f
            lector = csv.reader(f)          #lector permite recorrer el archivo fila por fila como una tabla, en este caso el archivo abierto f
            for i, fila in enumerate(lector):     #el for recorre el archivo linea por linea y el enumerate(lector) le da un numero a cada fila
                print(fila)
                if i == 14:        #se rompe en 14 porque solo nos piden las 15 primeras lineas
                    break
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo}")



def estadisticas_csv():
    archivo = "eventos_salud_publica.csv"
    columna = input("Ingrese el nombre de la columna: ")
    try:
        with open(archivo) as f:
            lector = csv.reader(f)
            encabezado = next(lector)    #para leer la primera fila de las columnas
            if columna not in encabezado:
                print("Columna no encontrada.")
                return
            indice = encabezado.index(columna)      #se usa para obtener el indice(la posicion de la columna)
            datos = []        #para guardar los datos numéricos de la columna

            for fila in lector:
                try:
                    valor = float(fila[indice])    #intenta convertir el valor del dato de la columna a un numero
                    datos.append(valor)    #si lo logra lo agrega a la lista
                except ValueError:
                    continue  # Ignora valores vacíos o no numéricos

            if datos:
                cantidad = len(datos)
                promedio = sum(datos) / cantidad
                mediana = sorted(datos)[cantidad // 2]
                minimo = min(datos)
                maximo = max(datos)

                print(f"Cantidad de datos: {cantidad}")
                print(f"Promedio: {promedio}")
                print(f"Mediana: {mediana}")
                print(f"Mínimo: {minimo}")
                print(f"Máximo: {maximo}")
            else:
                print("No hay datos numéricos en esa columna.")

    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo}")



def graficar_columna():
    archivo = "eventos_salud_publica.csv"
    columna = input("Ingrese el nombre de la columna a graficar: ")

    try:
        with open(archivo) as f:
            lector = csv.reader(f)        #lector que separa los datos por comas
            encabezado = next(lector)   #Lee la primera fila, que contiene los nombres de las columnas
            if columna not in encabezado:
                print("Columna no encontrada.")
                return
            indice = encabezado.index(columna)
            datos = []

            for fila in lector:
                try:
                    valor = float(fila[indice])
                    datos.append(valor)
                except ValueError:
                    continue
             #grafica
            if datos:
                plt.plot(datos)
                plt.title(f"Gráfico de la columna '{columna}'")
                plt.xlabel("Índice")
                plt.ylabel("Valor")
                plt.grid(True)
                plt.show()
            else:
                print("No se encontraron datos numéricos.")

    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo}")


def main():
    while True:
        opcion = menu_principal()

        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            opcion_submenu1 = submenu_txt()
            if opcion_submenu1 == "1":
                contar_txt()
            elif opcion_submenu1 == "2":
                reemplazar_palabra()
            elif opcion_submenu1 == "3":
                histograma_vocales()
            else:
                print("Opción no válida.")
        elif opcion == "3":
            opcion_submenu2 = submenu_csv()
            if opcion_submenu2 == "1":
                mostrar_csv()
            elif opcion_submenu2 == "2":
                estadisticas_csv()
            elif opcion_submenu2 == "3":
                graficar_columna()
            else:
                print("Opción no válida.")
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")



if __name__ == "__main__":
    main()