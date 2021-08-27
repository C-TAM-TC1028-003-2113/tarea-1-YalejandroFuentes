def main():
    # Este programa calcula el saldo mensual de una cuenta en este banco tomando en cuenta el saldo del mes anterior,
    # los ingresos, los egresos y el número de cheques expedidos.

    saldo = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el numero de cheques: "))

    saldo_final = saldo + ingresos - ((cheques * 13) + egresos)
    interes = saldo_final * 0.925

    print("El saldo final de la cuenta es:", interes)


if __name__ == '__main__':
    main()
