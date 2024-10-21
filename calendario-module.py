import csv
import calendar
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
month_days = calendar.monthcalendar(year, month)

cal = calendar.Calendar()
calendario = calendar.month(2024, 10)
print(calendario)
diaSemana_inicio, num_dias_mes = calendar.monthrange(year, month)

weekdays = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]

mes = []
rows = ["nombre"]
rows2 = [""]
contador = 0
dias = 0
diasArray = []
dias1 = [""]
dias2 = [""]

while len(mes) < 32:
    while contador < 1:
        for num in range(diaSemana_inicio, 7):
            mes.append(f"{weekdays[num]}")
            dias+= 1
            diasArray.append(dias)
            contador+= 1
    
    for num in range(7):
        if len(mes) < 32:
            mes.append(f"{weekdays[num]}")
            dias+= 1
            diasArray.append(dias)
        if len(diasArray) == num_dias_mes:
            dias = 0

for num in range(16):
    rows.append(mes[num])
    dias1.append(diasArray[num])

for num in range(16,32):
    rows2.append(mes[num])
    dias2.append(diasArray[num])
    

datos = [
    {'nombre': 'Alice'},
    {'nombre': 'Bob'},
    {'nombre': 'Charlie'}
]

# Crear el archivo CSV
with open(f'calendar_{month}_{year}-2.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=rows, delimiter=";")
    writer.writeheader()
    # Escribir los encabezados de los días de la semana
    writer.writerows(datos)

    # Escribir los días de cada semana
    #for week in month_days:
    #    writer.writerow(week)

