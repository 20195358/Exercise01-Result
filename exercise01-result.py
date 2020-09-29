# creando la lista vacia
listaRegistro = []
clientes = 0
# condición de parada
detener = "no"

while detener != "si":
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))

    # punto de programa
    # registro = {"cliente": cliente, "producto": producto, "costo": costo}
    registro = dict(cliente=cliente, producto=producto, costo=costo)
    # como agrego un elemento nuevo a una lista?
    listaRegistro.append(registro)
    # dejar de ocupar la variable registro
    # registro = None
    detener = input("¿Quiéres que se detenga el programa? si/no: ")
    clientes += 1

for registro in listaRegistro:
    print(registro)
