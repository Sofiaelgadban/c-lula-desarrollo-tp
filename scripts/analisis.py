with open("datos/dataset.csv", "r") as archivo:
    lineas = archivo.readlines()

total_ventas = 0

for linea in lineas[1:]:
    datos = linea.strip().split(",")

    producto = datos[0]
    cantidad = int(datos[1])
    precio = int(datos[2])

    total_ventas += cantidad * precio

print("Total de ventas:", total_ventas)

with open("resultados/resultado.txt", "w") as resultado:
    resultado.write(f"Total de ventas: {total_ventas}")
