'''Crear un programa que imprima en pantalla una tabla
de multiplicar utilizando un ciclo for.'''

num = int(input("Ingresa el numero de la tabla de multiplicar que quieres: "))
for i in range(1,11):
    print( num," x ", i, " = ", num*i)
