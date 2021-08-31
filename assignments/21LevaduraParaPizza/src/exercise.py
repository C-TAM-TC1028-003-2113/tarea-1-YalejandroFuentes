def main():
    # Este programa calcula la cantidad necesaria de levadura segun los gramos de harina.

    Gramos_de_harina = float(input("Dame la harina en gramos: "))

    Gramos_de_levadura = (Gramos_de_harina * 50) / 1000

    print("Necesitas estos gramos de levadura:", Gramos_de_levadura)


if __name__ == '__main__':
    main()
