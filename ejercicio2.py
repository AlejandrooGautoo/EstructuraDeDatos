
nota1 = float(input("Ingrese la nota del primer examen: "))
nota2 = float(input("Ingrese la nota del segundo examen: "))

promedio = (nota1 + nota2) / 2
print(f"El promedio es: {promedio:.2f}")

if nota2 >= 7:
    print("Aprobó el último examen.")
else:
    print("Desaprobó el último examen.")

if nota2 > nota1:
    print("Mejoró su desempeño.")
elif nota2 < nota1:
    print("Empeoró su desempeño.")
else:
    print("Mantuvo la nota.")

if promedio >= 7:
    print("El alumno promocionó la materia.")
elif promedio >= 4:
    print("El alumno debe rendir final.")
else:
    print("El alumno debe recursar.")

if __name__ == "__main__":
    
    pass