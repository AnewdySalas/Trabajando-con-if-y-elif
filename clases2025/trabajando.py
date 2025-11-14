
print("-"*40)
print("-------------Ejercicio #12--------------")
entrada = input("Introduce números separados por comas: ")

numeros_texto = entrada.split(',')  
numeros = []
for num in numeros_texto:
    numeros.append(float(num))  

suma = 0
for num in numeros:
    suma += num
media = suma / len(numeros)


suma_diferencias = 0
for num in numeros:
    diferencia = num - media
    suma_diferencias += diferencia ** 2  

varianza = suma_diferencias / len(numeros)
desviacion = varianza ** 0.5  

print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")

print("-"*40)