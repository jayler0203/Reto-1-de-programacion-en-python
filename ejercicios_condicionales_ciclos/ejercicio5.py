'''Crear un programa que reciba dos listas de números y
que genere una tercera lista que contenga la suma de
los elementos de las dos listas en la misma posición,
utilizando un ciclo for.'''
nums1 =[]
nums2 =[]
suma = []

cantidad = int(input("ingresa la candidad de numeros que quieres escribir en cada lista: "))
for i in range(cantidad):
    num =int(input("Ingrese un numero a la lista 1: "))
    nums1.append(num)   

for i in range(cantidad):
    num =int(input("Ingrese un numero a la lista 2: "))
    nums2.append(num)     
print("Lista 1: ",nums1)
print("Lista 2: ",nums2)
for i in range(len(nums1)):
    suma.append(nums1[i] + nums2[i])
print("La suma de los elementos de las dos listas en la cada posición es: ", suma)
