def calcular_costo(horas):
    if horas <= 4:
        return 6
    else:
        return 6 + (horas - 4) * 2

def main():
    # Solicitar al usuario el número de horas.
    horas = int(input("Ingrese el número de horas de estacionamiento: "))

    # Calcular el costo total
    total = calcular_costo(horas)

    # Mostrar el costo total
    print(f"El importe a pagar es: {total} soles.")

if __name__ == "__main__":
    main()
    

    