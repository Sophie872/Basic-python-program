anio = input("Ingrese una fecha empezando por año-mes-dia:  ")
from datetime import date
hoy = date.today()
fin_anio = date(2021, 12, 31)
faltan = fin_anio - hoy
faltan.days
print (f"El año termina en {faltan}")
#Lisbeth Mujica

