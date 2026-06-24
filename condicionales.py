import os

nombre = os.getenv("NAME")
edad = int(os.getenv("EDAD"))



if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")