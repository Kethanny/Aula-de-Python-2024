numeros_pares = []

for i in range(1, 1000):
    if i % 2 == 0:
       numeros_pares.append(str(i))

resultado = ", ".join(numeros_pares)
print(f"Números pares de 1 até 1000: {resultado}")