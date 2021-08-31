def main():
    # Este programa calcula el costo total mensual de un usuario del servicio telefonico.

    Mensajes = int(input("Dame el número de mensajes: "))
    Megas = float(input("Dame el número de megas: "))
    Minutos = int(input("Dame el número de minutos: "))

    CostoTotal= (Mensajes * 0.80) + (Megas * 0.80) + (Minutos * 0.80)

    print("El costo mensual es:", CostoTotal)

if __name__ == '__main__':
    main()
