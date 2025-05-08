from random import randint
lista1 = []
lista2 = []
for i in range(100):
    lista1.append(randint(0, 100))
    lista2.append(randint(50, 150))
conjunto1 = set(lista1)
conjunto2 =set(lista2)
elementos_iguales = conjunto1.intersection(conjunto2)
elementos_diferentes = conjunto1.difference(conjunto2)
lista3 = list(elementos_diferentes)
lista4 = list(elementos_iguales)
print(f"Los elementos iguales son {lista4}")
print(f"los elementos diferentes son {lista3}")