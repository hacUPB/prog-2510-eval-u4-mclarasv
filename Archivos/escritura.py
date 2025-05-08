nombre = input("ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
cedula = input("Ingrese su cédula: ")

var_archivo = open("C:\\Users\\B09S202est\\Desktop\\texto.txt","a")
var_archivo.write(f"{nombre} con cédula {cedula} tiene {edad} años\n")

var_archivo.close()