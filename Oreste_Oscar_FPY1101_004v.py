import random
import csv
import math


trabajadores = [
    {"nombre": "Juan Pérez"},
    {"nombre": "María García"},
    {"nombre": "Carlos López"},
    {"nombre": "Ana Martínez"},
    {"nombre": "Pedro Rodríguez"},
    {"nombre": "Laura Hernández"},
    {"nombre": "Miguel Sánchez"},
    {"nombre": "Isabel Gómez"},
    {"nombre": "Francisco Díaz"},
    {"nombre": "Elena Fernández"}
]



sueldos = []

def sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for k in range (10)]
    print ("\nSueldos Asignados")
    
def clasificar_sueldos():
    print("")
    print("Sueldos menosres a $800000 :", len([su for su in sueldos if su < 800000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo <800000:
            print (f"Nombre empleado: {trabajador["nombre"]} Sueldo: ${sueldo}")

    print("\nSueldos entre $800000 y $2000000:", len([su for su in sueldos if su > 800000 and su <2000000]))
    for trabajador, sueldo in zip(trabajadores,sueldos):
        if sueldo > 800000 and sueldo <2000000:
            print(f"Nombre empleado: {trabajador["nombre"]} Sueldo: ${sueldo}")
            
    print("\nSueldos mayores que $2000000 :", len([su for su in sueldos if su > 2000000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo >2000000:
            print (f"Nombre empleado: {trabajador["nombre"]} Sueldo: ${sueldo}")
            
    print("\nTOTAL SUELDOS: $", sum(sueldos))
    
    
def estadisticas():
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))

    print(f"\nSueldo más alto: ${sueldo_mas_alto}")
    print(f"\nSueldo más bajo: ${sueldo_mas_bajo}")
    print(f"\nPromedio de sueldos: ${sueldo_promedio}")
    print(f"\nMedia geométrica de sueldos: ${sueldo_geom}")
    
def reporte():
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajador["nombre"], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"Nombre empleado: {trabajador['nombre']} Sueldo Base: ${sueldo} Descuento Salud: ${descuento_salud} Descuento AFP: ${descuento_afp} Sueldo Líquido: ${sueldo_liquido}")



def salir_delprograma():
    print("\nPrograma finalizado")
    
    
def menu():
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        opcion = int(input("Seleccione una opción >>> "))

        if opcion == 1:
            sueldos_aleatorios()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            estadisticas()
        elif opcion == 4:
            reporte()
        elif opcion == 5:
            salir_delprograma()
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
