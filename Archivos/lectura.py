p_archivo_datos = open("texto2.txt","r")
archivo_imc = open("imc.txt","a")
for i in range(5):
    estatura = float(p_archivo_datos.readline())
    peso = int(p_archivo_datos.readline())
    imc = peso/estatura**2
    archivo_imc.write(str(imc)+"\n")

p_archivo_datos.close()
archivo_imc.close()