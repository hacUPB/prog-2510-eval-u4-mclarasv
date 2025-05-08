# Lista global para almacenar los diccionarios de personas
personas = []

def agregar_persona(nombre:str, edad:int, ciudad:str):
    persona = {
        'nombre': nombre,
        'edad': edad,
        'ciudad': ciudad
    }
    personas.append(persona)
    print(f"Diccionario: {personas[0]}")
    print(f"personas")

def main():
    name = input("Ingrese su nombre: ")
    age = int(input("Ingrese la edad: "))
    city = input("ingrese la ciudad: ")

    agregar_persona(name, age, city)
    agregar_persona("juan", 18, "medellín")

    print(f"Diccionario: {personas[0]}")
    print(f"Persona: {personas[1]["nombre"]}")

    for usuario in personas:           #inicio un bucle for
        if usuario["edad"] > 18:         #ingresa a la variable edad y verifica si es mayor de 18 años
            print(usuario["nombre"])        #si es asi va a ingresar a la variable nombre y lo va a imprimir

if __name__ == "__main__":
    main()