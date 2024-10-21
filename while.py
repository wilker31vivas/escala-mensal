
contador = 0
personas = []

while contador < 2:
    contador+= 1
    
    nombre = input("Dime el nombre de la persona")
    domingo = input("Trabaja el primer domingo?")
    while domingo != "si" and domingo != "no":
        domingo = input("Respuesta inválida. Por favor ingrese 'si' o 'no'.")
    dia = input("Dia de folga?")
    turno = input("Turno?")
    
    object = {
        "nombre": nombre,
        "domingo": domingo,
        "dia": dia,
        "turno": turno
    }
    
    personas.append(object)
    
print(personas)