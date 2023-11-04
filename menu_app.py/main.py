compras = []
total_gastado = 0

def agregar_compra(compras):
    append = int(input("Ingrese el monto de la compra: "))
    compras.append(append)
    print("Compra agregada correctamente.")

def mostrar_compras(compras):
    if not compras:
        print("La lista esta vacía, favor de ingresar valores de compra. ")
    for indice, listado in enumerate(compras, start=1):
        listado_formateado = "${:.2f}".format(listado)
        print(f"{indice}. {listado_formateado}")

def mostrar_total(compras):
    total_gastado = sum(compras)
    total_formateado = "${:.2f}".format(total_gastado)
    print("Total gastado: ", total_formateado)

def main():

    while True:
        print("Menú: ")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agregar_compra(compras)
        elif opcion == 2:
            mostrar_compras(compras)
        elif opcion == 3:
            mostrar_total(compras)
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

main()