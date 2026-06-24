import os

name = os.getenv("NOMBRE")
age = int(os.getenv("EDAD"))



if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")