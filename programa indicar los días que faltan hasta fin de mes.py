meses=input("ingrese un numero para seleccionar un mes: ")
	
if (meses=='enero' or meses=='marzo' or meses=='mayo' or meses=='julio' or meses=='octubre' or meses=='diciembre'):
	d=int(input("Ingrese el dia: "))
	d=31-d
	print(f"El mes de {meses} termina en {d}")

elif (meses=='abril' or meses=='junio' or meses=='septiembre' or meses=='noviembre'):
	d=int(input("Ingrese el dia: "))
	d=30-d
	print(f"El mes de {meses} termina en {d}")
	
elif (meses=='febrero'):
	d=int(input("Ingrese el dia: "))
	d=29-d
	print(f"El mes de {meses}termina en {d}")
	
else:
	print(f"mes o dia invadlido")

#Lisbeth Mujica
