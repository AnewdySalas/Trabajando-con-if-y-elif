nota = float(input("Cual es tu calificacion: "))

if nota  < 0 or nota > 100:
    print("la calificacion no esta dentro del rango definido")
    exit(0)
condicion = "Aprobado" if nota >= 70 else "Reprobado"

if nota >= 90:
    letra = "A"

elif nota >= 80:
    letra =  "B"

if nota >= 70:
    letra = "c"    

else:
    letra = "F"

print(nota, letra, condicion)
