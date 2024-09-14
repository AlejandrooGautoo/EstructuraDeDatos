def organizar_aulas(dia):
    if dia < 1 or dia > 6:
        return "Día inválido. Debe ser entre 1 y 6."

    if dia % 2 == 0:
        aula = "A-300"
    else:
        aula = "A-315"

    return aula

def calcular_cuota(turno, materias, cuota_original):
    if turno.lower() == 'tarde' and materias > 3:
        descuento = 0.25
    else:
        descuento = 0.05

    cuota_con_descuento = cuota_original * (1 - descuento)
    return cuota_con_descuento

def calcular_estacionamiento(transporte):
    transporte = transporte.strip().lower()
    if transporte in ['auto', 'moto']:
        costo = 300
    elif transporte == 'bicicleta':
        costo = 50
    else:
        return "Transporte no reconocido."

    return costo


if __name__ == "__main__":

    dia = int(input("Ingrese el número de día:1 (lunes) a 6 (sabado) : "))
    aula_asignada = organizar_aulas(dia)
    print(f"Aula asignada: {aula_asignada}")

    turno = input("Ingrese el turno : mañana, tarde o noche: ").strip().lower()
    materias = int(input("Ingrese el número de materias: "))
    cuota_original = float(input("Ingrese el valor de la cuota original: "))
    cuota_con_descuento = calcular_cuota(turno, materias, cuota_original)
    print(f"Valor de la cuota con descuento: {cuota_con_descuento:.2f}")

    transporte = input("Ingrese el vehiculo en el que ingrese:  auto, moto o bicicleta: ").strip().lower()
    costo_estacionamiento = calcular_estacionamiento(transporte)
    print(f"Costo de estacionamiento: {costo_estacionamiento}")