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


# 11. Calculo de impuesto 

while True:
    try:
        print("-"*20)
        print("Calculo de impuesto")
        print("-"*20)

        Salario = int(input("Ingresa tu salario: "))
        break
    except ValueError:
            print("Ingresa un numero valido")

if Salario <= 10000:
     print("Libre de impuestos.")

elif Salario > 10000 and Salario <= 30000:
 impuesto = 1000
 print(f"Su salario es {Salario} con {impuesto} de Impuesto.")

else:
    impuesto = 2000
    print(f"Su salario es {Salario} con {impuesto} de impuesto.")


# 12. Clasificacion de numeros

while True:
    try:
        print("-"*25)
        print("Clasificacion de numeros")
        print("-"*25)

        num1 = float(input("Ingresa el primer numero: "))

        num2 = float(input("Ingresa el segundo numero: "))

        Num3 = float(input("Ingresa el tercer numero: "))

        break
    except ValueError:
        print("Ingresa un numero valido.")  
555
if num1 > 0 and num2 > 0 and Num3 > 0:
 print("Numeros positivos.")

elif num1 < 0 and num2 < 0 and Num3 < 0:
   print("Numeros negativos.")

elif num1 == 0 or num2 == 0 or Num3 == 0:
   print("entre los numeros hay uno o mas con valor cero.")

else: 
   print("Numeros mixtos.")

# 13 Verificación de año bisiesto

while True:
    try:
        print("-"*25)
        print("Verificación de año bisiesto")
        print("-"*25)

        año = int(input("Ingresa el año: "))
        break

    except ValueError:
        print("Ingresa un año valido.")

if año %400 == 0:
    print("Es un año bisiesto")

elif año %100 == 0:
    print("No es un año bisiesto")

elif año  %4 == 0:
    print("Es un año bisiesto")

else:
    print("No es un año bisiesto")


    # 14. Conversion de calificacion

while True:
    try:
        print("-"*30)
        print("--Conversion de calificacion--")
        print("-"*30)

        calificacion = int(input("Ingresa tu calificacion: "))
        if calificacion < 0 or calificacion > 100:
         print("Calificacion fuera de los limites.")
        else:
           break
    except ValueError:
       print("Ingresa una calificacion valida.")  

if calificacion >= 90:
   print(f"{calificacion} A. Aprobado.")  

elif calificacion >= 80:
   print(f"{calificacion} B. Aprobado.")

elif calificacion >= 70:
   print(f"{calificacion} C. Aprobado.")

elif calificacion >= 60:
   print(f"{calificacion} D. Reprobado.")

else:
   print(F"{calificacion} F.Reprobado.")



# 15.  Comparación de tres longitudes 

while True:
    try:
        print("-"*35)
        print("--Comparación de tres longitudes--")
        print("-"*35)

        longitud1 = int(input("Ingresa longitud 1: "))
        longitud2 = int(input("Ingresa longitud 2: "))
        longitud3 = int(input("Ingresa longitud 3: "))
        break
    except ValueError:
        print("Ingresa un numero valido.")

if (longitud1 + longitud2 > longitud3) and (longitud2 + longitud3 > longitud1) and (longitud1 + longitud3 > longitud2):
    print("Es un triangulo.")

else:
    print("No es un triangulo.")

#16. Calculadora de descuentos 

while True:
        try:
          
          
          print("-"*33)
          print("===Calculadora de descuentos===")
          print("-"*33)

          producto = float(input("Ingresa precio del producto: "))

          if producto <= 0:
            print("El precio no puede ser menor o igual a 0.")
          else:
                break
        except ValueError: 
              print("Ingresa un precio valido.")
      

if producto < 50:
        print(f"Precio {producto} no aplica descuento.")
    
elif producto <= 100:
        descuento = producto * 0.05
        precio = producto - descuento
        print(f"Producto con descuento del 5%  precio de venta {precio}.")

else:
        descuento = producto * 0.10
        precio = producto - descuento
        print(f"Producto con descuento del 10%  precio de venta {precio}.")

# 17. Tipo de triángulo 

while True:
        try:
                  
          print("-"*30)
          print("===Tipo de triángulo===")
          print("-"*30)
          longitud1 = int(input("Ingresa longitud 1: "))
          longitud2 = int(input("Ingresa longitud 2: "))
          longitud3 = int(input("Ingresa longitud 3: "))

          if (longitud1 + longitud2 < longitud3) and (longitud2 + longitud3 < longitud1) and (longitud1 + longitud3 < longitud2):
            print("No es un triangulo.")        

          else:
              break
          
        except ValueError:
          print("Ingresa un numero valido.")


if longitud1 == longitud2 == longitud3:
    print("El triangulo es equilatero.")

elif longitud1 == longitud3 or longitud1 == longitud2 or longitud2 == longitud3:
    print("El triangulo es isosceles.")

else:
    print("El triangulo es escaleno")

    # 18. Evaluacion de temperatura

while True:
        try:
                  
          print("-"*30)
          print("===Evaluacion de temperatura===")
          print("-"*30)
          temperatura = float(input("Ingresa temperatura en (Grados Celcius): "))
          break

        except ValueError:
             print("Ingresa una temperatura valida.")

if temperatura < 0:
     print("Hace mucho frio.")

elif temperatura <= 20:
     print("Clima fresco")

elif temperatura <= 30:
     print("Clima agradable")

else:
     print("Hace mucho calor.")

# 19.  Conversión de horas a turnos

while True:
        try:
                  
          print("-"*30)
          print("=Conversión de horas a turnos=")
          print("-"*30)
          Hora = float(input("Ingresa hora (0 al 23): "))
          
          if Hora < 0 or Hora > 23:
               print("Ingresa una hora valida.")

          else: 
           break
        
        except ValueError:
             print("Ingresa una hora valida.")


if Hora <= 5:
    print("Madrugada.")

elif Hora <= 11:
    print("Mañana.")

elif Hora <= 17:
    print("Tarde.")

else:
    print("Noche.")

# 20.  Clasificación de IMC

print("-" *30)
print("Clasificacion de IMC")
print("-" *30)

peso  = float(input("Ingrese su peso en kilogramos (kg): "))
altura = float(input("Ingrese su altura en metros (m): "))

imc = peso / (altura ** 2)

print(f"Su IMC es: {imc}")
print("Clasificación:")


if imc < 18.5:
    
    print("Bajo peso")

elif imc >= 18.5 and imc <= 24.9:
    print("Peso Normal")

elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
    

elif imc >= 30:
    print("Obesidad")

