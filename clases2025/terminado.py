#Anewdy Salas Almonte 2025-0306

#1 Calculadora de Numeros

import math
while  True:
       
    
       print("="*40)   
       print("Calculadora de numeros") 
       print("="*40)

       print("1. Suma")
       print("2. Resta")
       print("3. Multiplcacion")
       print("4. Division")
       print("5. Modulo")
       print("6. Potencia")
       print("7. Raiz cuadrada")
       print("8. Salir")

       Opcion = int(input("elige una opcion (1-8): "))
       if Opcion == 8:
           print("Hasta luego")
           exit(0)
                
       break

if Opcion == 1:
  Num1 = float(input("Ingresa el primer numero: ")) 
  Num2 = float(input("Ingresa el segundo numero: "))
  Resultado = Num1 + Num2
  print(f"Resultado: {Num1} + {Num2} = {Resultado}")

elif Opcion == 2:
     Num1 = float(input("ingresa primer numero: "))
     Num2 = float(input("ingresa segundo numero: "))
     Resultado = Num1 - Num2
     print(f"Resultado: {Num1} - {Num2} = {Resultado}")

elif Opcion == 3:
      Num1 = float(input("ingresa primer numero: "))
      Num2 = float(input("ingresa segundo numero: "))      
      Resultado = Num1 * Num2
      print(f"Resultado: {Num1} * {Num2} = {Resultado}")

elif Opcion == 4:
      Num1 = float(input("ingresa primer numero: "))
      Num2 = float(input("ingresa segundo numero: ")) 
      if Num2 == 0:
       print("No se  puede dividir por cero")     
      Resultado = Num1 / Num2
      print(f"Resultado: {Num1} / {Num2} = {Resultado}")
    

elif Opcion == 5:
      Num1 = float(input("ingresa primer numero: "))
      Num2 = float(input("ingresa segundo numero: ")) 
      if Num2 == 0:
       print("No se  puede dividir por cero")     
      Resultado = Num1 % Num2
      print(f"Resultado: {Num1} % {Num2} = {Resultado}")

      
elif Opcion == 6:
      Num1 = float(input("ingresa primer numero: "))
      Num2 = float(input("ingresa segundo numero: ")) 
      Resultado = Num1 ** Num2
      print(f"Resultado: {Num1} ^ {Num2} = {Resultado}")
           
elif Opcion == 7:
       Num1 = float(input("Ingresa el numero: "))
       if Num1 < 0:
           print("No se puede calcular la raiz  de un numero negativo")
       else:
           Resultado = Num1 ** 0.5
           print(f"Resultado:  √{Num1} = {Resultado}")

else:
     print("Opcion no valida. el numero debe de ser entre del 1 al 8")







#2 Tabla de multiplicar hasta N
print("="*40)
print("Tabla de multiplicar")
print("="*40)

numero = int(input("Ingresa el número para la tabla de multiplicar: "))

limite = int(input("Ingresa hasta qué número quieres la tabla (Maximo 150): "))
if limite > 150:
    print("El limite para multiplicar es 150")
    exit(0)

print(f"Tabla de multiplicar del {numero} ")


for i in range(1, limite + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")   




#3 Validacion de contraseña
print("="*40)
print("Validacion de contraseña")
print("="*40)

contraseña = "Anewdy123"

usuario = input("Ingrese su nombre de usuario: ")
contraseña_ingresada = input("Ingrese su contraseña: ")

if contraseña_ingresada == contraseña:
    print(f"Bienvenido {usuario}")
else:
    print("Contraseña incorrecta. Acceso denegado.")



    #4 El mayor de 3 numeros
print("="*30)    
print("El mayor de los 3")
print("="*30)

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print(f"El número mayor es: {mayor}")



#5  Calculadora de Temperatura
print("="*40)
print("Calculadora de teamperatura")
print("="*40)

print("--- Fahrenheit a Celsius ---")
fahrenheit = float(input("Ingresa los grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Resultado:", celsius, "grados Celsius")

print("--- Celsius a Fahrenheit ---")
celsius = float(input("Ingresa los grados Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Resultado:", fahrenheit, "grados Fahrenheit")

print("Adios")
    

        



       
          



