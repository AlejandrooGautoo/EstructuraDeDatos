print("=== Registro de Inscripciones de Alumnos ===")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")

tiene_titulo_secundario = True 

monto_matricula = float(input("Ingrese el monto de matrícula: "))

cuota = monto_matricula + 1000

materia_python_i = 12000
costo_mensual = cuota + materia_python_i

pago_efectivo = input("¿Pagará en efectivo? (si/no): ").strip().lower()
if pago_efectivo == 'si':
    descuento = costo_mensual * 0.15
    costo_mensual -= descuento

print("\n=== Datos del Alumno ===")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Fecha de Nacimiento: {fecha_nacimiento}")
print(f"Tiene Título Secundario: {tiene_titulo_secundario}")
print(f"Monto de Matrícula: ${monto_matricula:.2f}")
print(f"Cuota: ${cuota:.2f}")
print(f"Costo Mensual (con descuento si aplica): ${costo_mensual:.2f}")