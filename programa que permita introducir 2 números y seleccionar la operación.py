def calculadora(operacion, a, b):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a -b
    elif operacion == "multiplicar":
        return a * b
    elif operacion == "division":
        return a/b
    else:
        return "Operación no válida"

operacion = input("Elija una operación;suma, resta, multiplicar, division:")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print(f"La operacion a escoger es: {operacion}")
print("El resultado es: ",calculadora(operacion, num1, num2))

#Lisbeth Mujica
