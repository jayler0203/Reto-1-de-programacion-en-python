# Crea un programa que le pida al usuario que ingrese un número entero.
# Si el número es par, imprime "El número es par".
# Si el número es impar, imprime "El número es impar".
num = int(input("Ingresa un numero entero: "))
if num%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")