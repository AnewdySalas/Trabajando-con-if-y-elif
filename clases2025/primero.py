nota = float(input("Ingresa la Calificacion: "))

if nota < 0 or nota >100:
    print("La calificacion no está dentro del rango definido")
    exit(0)    

estado = "Aprobado" if nota >= 70 else "Reprobado"

if nota >= 90:
    letra = "A exlente,"

elif nota >= 80:
    letra = "B muy bien,"   

elif nota >= 70:
    letra = "C debes mejorar,"

elif nota <= 69:
    letra = "F hechale mas ganas,"
    
    
print(nota, letra, estado)


