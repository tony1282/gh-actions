import os
nombre = os.getenv("USERNAME")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print(f"{nombre} eseres mayor de edad.")
else:
    print(f"{nombre} eres menor de edad.")