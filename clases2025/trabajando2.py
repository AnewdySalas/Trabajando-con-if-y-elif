# 9. Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle while.
#  El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.

while True:
    try:

        Numero = int(input("Ingresa numero:"))
        if Numero < 0:
            print("El numero debe ser mayor a 0.")
        else:
            break

    except ValueError:
        print("Ingresa un numero valido.")

factorial = 1

for i in range(1, Numero + 1):

    factorial *= i
    
print(f"El factorial de {Numero} es: {factorial}")

        

        