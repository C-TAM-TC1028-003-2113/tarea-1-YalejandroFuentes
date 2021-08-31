def main():
    # Este programa calcula el costo de una publicacion a partir de las palabras mismas.

    Palabras = int(input("Dame el número de palabras: "))

    Paginas = Palabras // 475
    Paginas_totales = Paginas + 1
    Costo = Paginas_totales * (60 * .9)

    print("El costo de la publicacion es:", Costo)


if __name__ == '__main__':
    main()
