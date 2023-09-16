'''Crear un programa que recibauna lista de números y calcule
la suma de los mismos utilizando un ciclo for.'''
nums =[]
salir = True
while salir:
    num =int(input("Ingrese un numero a la lista. Ingrese 0 si desea terminar "))
    if num != 0:
        nums.append(num)     
    else:
        salir=False
suma = 0
for num in nums:
    suma+= num
print("La suma de los numeros",nums, " es ",suma)