ganancias = float(input("Ingrese las ganancias de Pablito: "))

if 0 <= ganancias <= 1000:
    porcentaje = 5
elif 1000 < ganancias <= 1500:
    porcentaje = 7  # Corrección aquí
elif 1500 < ganancias <= 2000:
    porcentaje = 8
elif 2000 < ganancias <= 5000:
    porcentaje = 10
else:
    porcentaje = 15

donativo = ganancias * (porcentaje / 100)
print(f"Pablito donará el {porcentaje}% de sus ganancias, es decir, {donativo} soles.")


