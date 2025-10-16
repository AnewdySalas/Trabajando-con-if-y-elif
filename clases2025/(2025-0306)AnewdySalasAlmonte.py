# 1. Numero positivo, negativo o cero
while True:
    try:
        print("="*50)
        print("---Verificar numero positivo negativo o cero---")
        print("="*50)

        Numero = float(input("Ingresa numero: "))

        break
    except ValueError:
        print("Error. Ingresa un numero valido")

if Numero < 0:
    print(f"El numero {Numero} es negativo")

elif Numero > 0: 
    print(f"El numero {Numero} es positivo")    

else:
    print("El numero es 0")    
  


 # 2. Numero par o impar
while True:
    try:
        print("-"*30)
        print("--Verificacion de par o impar--")
        print("-"*30)

        Numero = float(input("Ingresa numero: "))
        break
    except ValueError:
        print("Debes ingresar un numero")

if Numero %2==0:
    print(f"El numero {Numero} es par.")

else:
    print(f"El numero {Numero} es impar")



# 3. Mayor de edad

while True:
    try:
        print("="*30)
        print("-----Verificacion de edad-----")
        print("="*30)

        edad = int(input("Ingresa tu edad: "))
        if edad < 0 or edad > 150:
            print("Edad fuera de los limites. Ingresa un valor valido")
        else:
            break
    except ValueError:
        print("Debes ingresar un numero entero valido")  

if edad < 18:
    print(f" {edad} Años, eres menor de edad")          

else:
    print(f"{edad} Años, eres mayor de edad")


# 4. Multiplo de 5
while True:
    try:
        print("-"*40)
        print("Verificar si el numero es multiplo de 5")
        print("-"*40)

        Numero = float(input("Ingrese el numero: "))
        break

    except ValueError:
        print("Ingrese un numero valido")
    
if Numero %5==0:
    print(f"{Numero} es un multiplo de 5")

else:
    print(f"{Numero} no es un mulptiplo de 5")


# 5. Descuento por edad
while True:
    try:
        print("-"*30)
        print("Descuento por edad")
        print("-"*30)

        Edad = int(input("Ingresa tu edad: "))
        if Edad < 0 or Edad > 150:
            print("Edad fuera de los limites.")
        else:
            break
        
    except ValueError:
        print("Ingresa un numero valido.")
    

if Edad < 60:
    print("No aplica para descuento.")

else:
    print("Aplica para descuento.") 


# 6. Calificación aprobatoria 

while True:
    try:
        print("-"*30)
        print("-Calificación aprobatoria-")
        print("-"*30)

        Calificacion = int(input("Ingresa tu calificacion: "))
        if Calificacion < 0 or Calificacion > 100:
            print("Calificacion fuera de los limites.")
        else:
            break
        
    except ValueError:
        print("Ingresa unaCalificacion valida.")
    

if Calificacion < 60:
    print(f"{Calificacion}, Estas Reprobado.")

else:
    print(f"{Calificacion}, Estas aprobado.")    


 # 7. Dia de la semana
while True:
    try:
        print("-"*20)
        print("--Dia de la semana--")
        print("-"*20)

        Opcion = int(input("Elige una opcion del (1-7): "))

        if Opcion < 1 or Opcion > 7:
            print("Tu opcion esta fuera de los limites.")
        else:
            break
    except ValueError:
        print("Escibe una opcion valida.")
    
if Opcion == 1:
    print("Es lunes.")

elif Opcion == 2:
    print("Es martes.")

elif Opcion == 3:
    print("Es miercoles.")

elif Opcion == 4:
    print("Es jueves.")

elif Opcion == 5:
    print("Es viernes.")

elif Opcion == 6:
    print("Es sabado")

else:
    print("Es domingo")   


# 8. Mayor entre dos numeros 

while True:
    try:
        print("-"*30)
        print("---Cual es mayor de los dos---")
        print("-"*30)

        Numero1 = float(input("Ingresa el primer numero: "))
        Numero2 = float(input("Ingresa el segundo numero: "))
        break
    except ValueError:
        print("ingresa un numero valido.")

if Numero1 > Numero2:
    print(f"El {Numero1} es mayor.")

elif Numero2 > Numero1:
    print(f"El {Numero2} es mayor.")  

else:
    print("Los numeros son iguales.")  


# 9. Mayor entre tres números 
while True:
    try:
        print("-"*30)
        print("--Cual es mayor de los tres--")
        print("-"*30)

        Numero1 = float(input("Ingresa el primer numero: "))
        Numero2 = float(input("Ingresa el segundo numero: "))
        Numero3 = float(input("Inf¿gresa el tercer numero: "))
        break
    except ValueError:
        print("Ingresa un numero valido.")

if Numero1 >= Numero2 and Numero1 >= Numero3:
    print(f"El {Numero1} es mayor")

elif Numero2 >= Numero1 and Numero2 >= Numero3:
    print(f"El {Numero2} es mayor")

else:
    print(f"El {Numero3} es mayor.")


# 10. Clasificación de ángulos 

while True:
    try:
        print("-"*25)
        print("Clasificación de ángulos")
        print("-"*25)
        
        Medida = int(input("Ingresa la medida (en grados): "))
        if Medida < 0 or Medida > 180:
            print("Medida fuera de los limites.")
        else:
            break
    except ValueError:
        print("Escriba una medida valida.")

if Medida < 90:
    print("El angulo es agudo.")

elif Medida == 90:
    print("El angulo es recto.")

elif Medida == 180:
    print("El angulo es llano.")
 
else:
    print("El angulo es obtuso.")


