while True:
    try:
        numero = int(input("verificar numero:"))
        break
    except ValueError:
     print("Error: debes agregar un numero")   
   
if numero %2==0:
    print("El numero es par")

else:
   print("El numero es impar")    