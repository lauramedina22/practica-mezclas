nombre = "Mundo"
print("Hola, " + nombre + "!")
print("Soy Lilith")
print("Soy Laura")


print("Comparacion, mayor o menor")
num1 = 5
num2 = 10

if num1 < num2:
    print("num1 es menor que num2")
else:
    print("num1 no es menor que num2")
    
print("Bienvenido a la calculadora :)")
    
print("CALCULADORA")
operacion = input("Elige una operacion (suma, resta, multiplicacion, division): ")
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
resultado = 0
if operacion == "suma":
    resultado = num1 + num2
elif operacion == "resta":
    resultado = num1 - num2
elif operacion == "multiplicacion":
    resultado = num1 * num2
elif operacion == "division":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Error: No se puede dividir entre cero.")
