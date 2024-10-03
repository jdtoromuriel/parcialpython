NombreConductor = []
DiasSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
Recaudo = []
TotalRecaudo = []

while True:
    try:
        num_conductores = int(input("Ingrese el número de conductores: "))
        if num_conductores > 0:
            break
        else:
            print("Por favor, ingrese un número positivo.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

for i in range(num_conductores):
    nombre = input(f"Ingrese el nombre del conductor {i + 1}: ")
    NombreConductor.append(nombre)
    
    recaudo_por_dia = []
    print(f"Ingrese el recaudo de {nombre} por día:")
    
    for dia in DiasSemana:
        while True:
            try:
                recaudo = float(input(f"{dia}: "))
                recaudo_por_dia.append(recaudo)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

    Recaudo.append(recaudo_por_dia)
    
    total = sum(recaudo_por_dia)
    TotalRecaudo.append(total)

print("\nResumen de Recaudo por Conductor:")
for i in range(num_conductores):

    print(f"Número de Conductor: {i + 1} - Nombre: {NombreConductor[i]} - Total Recaudado: ${TotalRecaudo[i]:.2f}")