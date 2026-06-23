import os

nombre = os.getenv("USERNAME", "Invitado")
edad = int(os.getenv("EDAD", "0"))

if edad >= 18:
    print(f"{nombre} eres mayor de edad.")
else:
    print(f"{nombre} eres menor de edad.")
