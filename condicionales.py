# Número positivo o negativo
numero = float(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Par o impar
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Mayor de dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2:
    print(f"El número {num1} es mayor.")
elif num2 > num1:
    print(f"El número {num2} es mayor.")
else:
    print("Los números son iguales.")

# Clasificación de edad
edad = int(input("Ingrese la edad: "))
if edad < 13:
    print("Eres un niño.")
elif edad < 20:
    print("Eres un adolescente.")
elif edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un anciano.")

# Aprobado o reprobado
calificacion = float(input("Ingrese la calificación: "))
if calificacion >= 6:
    print("Aprobado.")
else:
    print("Reprobado.")

# Múltiplo de 3 y/o 5
numero = int(input("Ingrese un número: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("El número es múltiplo de 3 y 5.")
elif numero % 3 == 0:
    print("El número es múltiplo de 3.")
elif numero % 5 == 0:
    print("El número es múltiplo de 5.")
else:
    print("El número no es múltiplo de 3 ni 5.")

# Comparar tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
if num1 >= num2 and num1 >= num3:
    print(f"El número {num1} es el mayor.")
elif num2 >= num1 and num2 >= num3:
    print(f"El número {num2} es el mayor.")
else:
    print(f"El número {num3} es el mayor.")

# Calculadora simple
num1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (+, -, *, /): ")
num2 = float(input("Ingrese el segundo número: "))
if operador == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operador == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operador == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operador == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: división por cero.")
else:
    print("Operador inválido.")

# Verificar año bisiesto
año = int(input("Ingrese el año: "))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")

# Validar contraseña
contraseña_establecida = "mi_contraseña"
contraseña_ingresada = input("Ingrese la contraseña: ")
if contraseña_ingresada == contraseña_establecida:
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")