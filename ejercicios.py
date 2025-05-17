#Nivel facil
def saludo():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}!")

saludo()

def suma():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print(f"La suma es: {resultado}")

suma()

def par_o_impar():
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

par_o_impar()


def mayoria_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

mayoria_edad()

def celsius_a_fahrenheit():
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"La temperatura en Fahrenheit es: {fahrenheit}")

celsius_a_fahrenheit()

def area_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")

area_triangulo()

def mayor():
    lista = input("Ingrese una lista de números separados por espacios: ")
    lista = [float(x) for x in lista.split()]
    maximo = max(lista)
    print(f"El mayor número de la lista es: {maximo}")

mayor()

def contar_letras():
    palabra = input("Ingrese una palabra: ")
    letra = input("Ingrese la letra que desea contar: ")
    resultado = palabra.count(letra)
    print(f"La letra '{letra}' aparece {resultado} veces en la palabra '{palabra}'")

contar_letras()

#nivel intermedio

def filtrar_pares():
    lista = input("Ingrese una lista de números separados por espacios: ")
    lista = [int(x) for x in lista.split()]
    pares = [x for x in lista if x % 2 == 0]
    print(f"Los números pares de la lista son: {pares}")

filtrar_pares()

def es_palindromo():
    texto = input("Ingrese un texto: ")
    if texto == texto[::-1]:
        print("El texto es un palíndromo")
    else:
        print("El texto no es un palíndromo")

es_palindromo()

def factorial():
    num = int(input("Ingrese un número: "))
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    print(f"El factorial de {num} es: {resultado}")

factorial()

def eliminar_duplicados():
    lista = input("Ingrese una lista de números separados por espacios: ")
    lista = [int(x) for x in lista.split()]
    sin_duplicados = list(set(lista))
    print(f"La lista sin duplicados es: {sin_duplicados}")

eliminar_duplicados()

def fizzbuzz():
    num = int(input("Ingrese un número: "))
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

fizzbuzz()

def contar_vocales():
    texto = input("Ingrese un texto: ")
    vocales = "aeiou"
    resultado = sum(1 for char in texto.lower() if char in vocales)
    print(f"El texto tiene {resultado} vocales")

contar_vocales()

def invertir_texto():
    texto = input("Ingrese un texto: ")
    resultado = texto[::-1]
    print(f"El texto invertido es: {resultado}")

invertir_texto()

#nivel avanzado


