import math
while True:


    print("="*40)
    print("Calculadora de numeros")
    print("="*40)

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Modulo")
    print("7. Raiz cuadrada")
    print("8. Salir")

    Opcion = int(input("ingresa un numero del 1 al 8: "))

    
    break


if Opcion == 1:
    Num1 = float(input("Ingresa el primer numero: "))
    Num2 = float(input("Ingresa el segundo numero: "))
    Resultado = Num1 + Num2
    print(f"Resultado: {Num1} + {Num2} = {Resultado}")


elif Opcion == 2:
    Num1 = float(input("Ingresa el primer numero: "))
    Num2 = float(input("Ingresa el segundo numero: "))
    Resultado = Num1 - Num2
    print(f"Resultado: {Num1} - {Num2} = {Resultado}")


elif Opcion == 3:
    Num1 = float(input("Ingresa el  primer numero: "))
    Num2 = float(input("Ingresa el segundo numero: "))
    Resultado = Num1 * Num2
    print(f"Resultado: {Num1} * {Num2} = {Resultado}")


elif Opcion == 4:
    Num1 = float(input("Ingresa el primer numero: "))
    Num2 = float(input("Ingresa el segundo numero: "))
    if Num2 == 0:
        print("No se puede dividir por cero")
    Resultado = Num1 / Num2
    print(f"Resultado: {Num1} / {Num2} = {Resultado}")


elif Opcion == 5:
    Num1 = float(input("Ingresa el primer numero: "))   
    Num2 = float(input("Ingresa el segundo numero: ")) 
    Resultado = Num1 ** Num2
    print(f"Relsultado: {Num1} ^ {Num2} = {Resultado}")


elif Opcion == 6:
    Num1 = float(input("Ingresa el primer numero: "))    
    Num2 = float(input("Ingresa el segundo numero: "))
    if Num2 == 0:
        print("No se puede dividir por cero")
    Resultado = Num1 % Num2
    print(f"Resultado: {Num1} % {Num2} = {Resultado}")

elif Opcion == 7:
    Num1 = float(input("Ingresa el numero: "))
    if Num1  < 0:
        print("No se puede buscar raiz a  un numero neativo")
    else:
         Resultado = Num1 ** 0.5
         print(f"Resultado:  √{Num1}  = {Resultado}")

elif Opcion == 8:   
    print("Hasta luego")
    exit(0)      

else:
    print("Error: Elige un numero del 1 al 8")
    



              