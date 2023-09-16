# Crear un programa que reciba una lista de palabras y
# muestre únicamente aquellas que empiezan con una letra
# determinada, utilizando un ciclo for y una estructura condicional if.
palabras =[]
salir = True
while salir:
    palabra =input("Ingrese un palabra a la lista. Ingrese salir si desea terminar ")
    if palabra.lower() != "salir":
        palabras.append(palabra)     
    else:
        salir=False
inicial = input("Ingresa la inicial de las palabras que quieres mostrar")
palabrasfilt=[]
for palabra in palabras:
    if inicial==palabra[0]:
        palabrasfilt.append(palabra)
print("las palabras con la inicial ", inicial," son ", palabrasfilt)       