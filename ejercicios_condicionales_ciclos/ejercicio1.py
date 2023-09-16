'''Crea una lista de 5 nombres de frutas.
Utiliza un ciclo for para imprimir en pantalla cada uno de los nombres de la lista.
Utiliza otro ciclo for para imprimir en pantalla cada letra de cada uno de los nombres de la lista.''' 
frutas = ["manzana", "banana", "fresa", "uva", "naranja"]
for fruta in frutas:
    print(fruta)
for fruta in frutas:
    for l in fruta:
        print(l) 
    print("")
