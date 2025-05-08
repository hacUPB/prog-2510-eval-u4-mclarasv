usuarios = {
    "user1": {"nombre": "Ana", "edad": 25},
    "user2": {"nombre": "Luis", "edad": 30}
}
print(usuarios["user1"]["edad"])
user3 = {}
nombre = input("escriba su nombre:")
edad = int(input("escriba su edad:"))
user3["nombre"] = nombre
user3["edad"] = edad
print(user3)
usuarios["user3"] = user3
print(usuarios)