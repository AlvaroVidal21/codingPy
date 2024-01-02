

lista = ["S-Sherlock", "S-Mycroft"]

print(lista)

index = 0
for l in lista:
    lista[index] = lista[index].replace('S-', '')
    index += 1

print(lista)
   