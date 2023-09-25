def suma_primeros_n_naturales(n):
    return n * (n + 1) // 2

def main():
    n = int(input("Ingrese el valor de n: "))
    total = suma_primeros_n_naturales(n)
    print(f"La suma de los primeros {n} números naturales es: {total}")

if __name__ == "__main__":
    main()