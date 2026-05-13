print("PROGRAMA DE CALIFICACIONES S&S:)")

nombre = input("Ingrese el nombre del estudiante: ")

suma = 0

for contador in range(1, 6):

    if contador == 1:
        nota = input("Ingrese la primera nota: ")

    elif contador == 2:
        nota = input("Ingrese la segunda nota: ")

    elif contador == 3:
        nota = input("Ingrese la tercera nota: ")

    elif contador == 4:
        nota = input("Ingrese la cuarta nota: ")

    else:
        nota = input("Ingrese la quinta nota: ")

    nota = float(nota)

    suma = suma + nota