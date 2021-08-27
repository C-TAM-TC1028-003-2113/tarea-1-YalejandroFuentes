def main():
    # Este programa calcula el total de la compra de los videojuegos nuevos y usados.

    JuegosNuevos = int(input("Dame la cantidad de juegos nuevos: "))
    JuegosUsados = int(input("Dame la cantidad de juegos usados: "))

    Total = (1000 * JuegosNuevos) + (350 * JuegosUsados)

    print("El total de la compra es:", Total)


if __name__ == '__main__':
    main()
