import datetime
date_string = input("Ingrese una fecha empezando  por: %Y-%m-%d ")
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format)
  print("La fecha es valida")
except ValueError:
  print("La fecha es invalida")
  
#Lisbeth Mujica
