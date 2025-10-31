# ==============================================
#       SISTEMA DE CORTE DE CAJA
# ==============================================

# Solicitar fecha
while True:
    fecha = input("Ingresa la fecha del corte (DD/MM/AAAA): ")
    if fecha.strip() != "":
        break

# Ingreso de billetes
print("----------------------------------------------")
print("        INGRESO DE BILLETES")
print("----------------------------------------------")

b1000 = int(input("Billetes de $1000: "))
b500 = int(input("Billetes de $500: "))
b200 = int(input("Billetes de $200: "))
b100 = int(input("Billetes de $100: "))
b50 = int(input("Billetes de $50: "))
b20 = int(input("Billetes de $20: "))

# Ingreso de monedas
print("----------------------------------------------")
print("        INGRESO DE MONEDAS")
print("----------------------------------------------")

m10 = int(input("Monedas de $10: "))
m5 = int(input("Monedas de $5: "))
m2 = int(input("Monedas de $2: "))
m1 = int(input("Monedas de $1: "))
m050 = float(input("Monedas de $0.50: "))

# Calcular total
total = (b1000 * 1000 + b500 * 500 + b200 * 200 + b100 * 100 +
          b50 * 50 + b20 * 20 + m10 * 10 + m5 * 5 + m2 * 2 +
          m1 * 1 + m050 * 0.5)

print("==============================================")
print("TOTAL DE DINERO CONTADO: $", round(total, 2))

# Solicitar fondo con validación
while True:
    fondo = float(input("¿Cuánto deseas dejar de fondo en caja? "))
    if fondo > total:
        print("Error: No puedes dejar más dinero del que tienes en caja. Intenta de nuevo.")
    else:
        break

# Calcular dinero para sobre
sobre = total - fondo

# Mostrar resultados finales
print("----------------------------------------------")
print("DINERO CONTADO: $", round(total, 2))
print("DINERO PARA FONDO: $", round(fondo, 2))
print("DINERO PARA SOBRE: $", round(sobre, 2))
print("FECHA DEL CORTE:", fecha)
print("==============================================")
print("CORTE FINALIZADO CORRECTAMENTE")