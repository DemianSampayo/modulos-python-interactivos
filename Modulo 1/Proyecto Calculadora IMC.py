peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Estás por debajo del peso normal.")
elif 18.5 <= imc < 24.9:
    print("Tienes un peso normal.")
elif 25 <= imc < 29.9:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")
print("Gracias por usar la calculadora de IMC.")
# Fin del proyecto: Calculadora de IMC