# 1. Escribe un programa que pida al usuario que ingrese un número entero positivo.
# El programa debe mostrar todos los números del 1 hasta el número ingresado, uno por uno, utilizando un bucle while.

print("Secuencia de numeros")
Numero = int(input("Ingresa un numero  entero positivo: "))

if Numero  >  0:
    print(f"Mostrando numero del 1 hasta {Numero}.")

    contador = 1

while contador <= Numero:
    print(contador)
    contador += 1

else:
   print("El numero debe de se mayor a 0.")

print("Terminado")

# 2. Escribe un programa que imprima los números pares entre 1 y 20 
# (inclusive) utilizando un bucle for.


print("NUMEROS PARES DEL 1 AL 20:")

for numero in range(2, 21, 2):
    print(numero)

print("Terminado")

# 3. Escribe un programa que pida al usuario un número entero positivo. El programa
# debe contar cuántos dígitos tiene el número utilizando un bucle while.

while True:
    try:
      
      print("CONTADOR DE NUMERO")

      Numero = int(input("Ingresa un numero: "))
      if Numero < 0:
         print("El numero debe ser mayor a 0.")
      else:
        break

    except ValueError:
       print("Ingresa un numero valido.")

Contador = 0

if Numero == 0:
   Contador = 1

else:
   
   while Numero > 0:
      Numero = Numero // 10
      Contador  += 1


      
print(f"El numero tiene {Contador} digitos.")

# 4. Escribe un programa que calcule la suma de todos los números enteros del 1 al 100 utilizando un bucle for.
Numero = 0

for  Contador in range (1, 101, 1):
   Numero = Numero + Contador
   print(Contador)

print(f"La suma de los numeros del 1 al 100 es {Numero}. ")

# 5. Escribe un programa que pida al usuario un número entero y luego imprima todos los 
# números desde ese número hasta el 0 en orden descendente utilizando un bucle while.
print("NUMEROS DESCENDENTES")

numero = int(input("Ingresa un número entero: "))

while numero >= 0:
    print(numero)
    numero -= 1  

# 6. Escribe un programa que imprima la tabla de multiplicar de un número dado
#  por el usuario, desde el 1 hasta el 10, utilizando un bucle for.

numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
if numero < 0 or numero > 10:
    print("Ingresa un numero valido.")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7.  Escribe un programa que pida al usuario un número entero positivo y 
# luego imprima todos los números impares desde 1 hasta el número ingresado utilizando un bucle while.

print("Verificacion de numeros impares")
while True:
    try:
      numero = int(input("Ingresa un número entero positivo: "))
      if numero < 0:
         print("El numero de ser mayor a 0.")
      else:
         break
    except ValueError:
       print("Ingresa un numero valido.")  


contador = 1

while contador <= numero:
    print(contador)
    contador += 2 

# 8. Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término, donde
# el valor de n lo ingresa el usuario, utilizando un bucle for.
print("Serie Fibonacci")
while True:
   try:

     n = int(input("Ingresa el número de términos de la serie Fibonacci: "))
     if n < 0:
        print("El numero debe ser mayor a 0")
     else:
        break
     
   except ValueError:
      print("El numero debe ser un entero positivo")


a, b = 0, 1


for i in range(n):
    print(a)
    a, b = b, a + b  

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





# 10. Escribe un programa que pida al usuario ingresar una contraseña y repita la solicitud
#  mientras la contraseña ingresada sea incorrecta.El programa debe continuar hasta que el usuario ingrese la contraseña correcta.
#  Utiliza una estructura while para simular un do while.


contraseña = "1234"

while True:
    Usuario = input("Ingresa la contraseña: ")
    if Usuario == contraseña:
        print("Contraseña correcta")
        break  
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")
   
