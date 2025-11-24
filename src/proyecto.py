    # ---PROYECTO FINAL---


def pedir_entero (prompt,minimo=None, Maximo=None):
    while True:
        try:
            v= int(input(prompt))
            if minimo is not None and v < minimo:
                print(f"(ERROR) Debe ser >= {minimo}.")
                continue
            if Maximo is not None and v > Maximo:
                print(f"(ERROR) Debe ser <= {Maximo}.")
                continue
            return v
        except ValueError:
            print("Entrafa invalida. Ingresa un numero entero.")

def pedir_float (prompt, minimo = None):
    """"Pide un número (float) con validación y devuelve el valor."""
    while True:
        try:
            v = float(input(prompt))
            if minimo is not None and v < minimo :
                print(f"(Error) Debe ser >={minimo}.")
                continue
            return v
        except ValueError:
            print("Entrada invalida. Ingresa un número válido.")


def mostrar_menu_principal():


def resistrar_ventas ():
    global total_general
    num_clientes = pedir_entero ("¿Cuántos clientes se registrarán hoy? (0 para volver): ", minimo=0)
    if num_clientes == 0:
        return
    
    for i in range (num_clientes):
        print ("\n------------------------------------------------------------------------------")
        print (f"\n                            CLIENTE {i+1}")
        print ("\n------------------------------------------------------------------------------")
        nombre = input ("Ingresa nombre: ").strip()
        edad = pedir_entero ("Ingresa la edad: ", nombre)

        print ("\nPelículas disponibles")
        print ("\n1. Spiderman")
        print ("\n2. Terrifier 3")
        print ("\n3. PacMan")

        pelicula_op = input ("Elige una película (1-3): ").strip()

    if pelicula_op == "1":
        pelicula = "spiderman"
    elif pelicula_op == "2":
        pelicula = "Terrifier 3" \
    elif pelicula_op == "3":
        pelicula = "PacMan"
    else:
        print ("Número inválido")

    peliculas_contador [pelicula] += 1


    print ("\n Combos disponibles")
    print ("\n 1. Palomitas con Coca-cola - $250")
    print ("\n 2. Palomitas y dos raspados - $ 280")
    print ("\n 3. Palomitas y nachos - $")
    combo_op = input ("Elige un combo (1-3): ").strip()
    if combo_op == "1":
        combo = "Palomitas con Coca-cola"
    elif combo_op == "2":
        combo = "Palomitas y dos raspados"
    elif combo_op == "3":
        combo = "Palomitas y nachos"
    else:
        print ("Número inválido")

    precio_combo = combos_precios[combo]
    combos_contador [combo] += 1
    total_cliente = precio_combo

    total_general += total_cliente

    print ("\nRegistro de cliente")
    print ("Nombre:", nombre)
    print ("Edad", edad)
    print ("Película", pelicula)
    print ("Combo", combo)
    print ("Total a pagar: $", round(total_cliente, 2))


def determinar_mas_vendido ():


def mostrar_resumen ():
    """"Muestra un resumen sencillo del día.""""
    print("\n================================================")
    print("         R E S U M E N   D E L    D I A    ")
    print("\n================================================")
    peli_top = determinar_mas_vendido(peliculas_contador)
    combo_top = determinar_mas_vendido(combos_contador)

    if peli_top is None:
        print("Peliculas más vista: Ninguna venta aún.")
    elif isinstance(peli_top, list):
        print("Peliculas más vistas (empatadas):",",".join(combo_top))
    else:
        print("Combo más vendido:", combo_top)

        print("TOTAL DE VENTAS DEL DIA: $", round(total_general, 2))
        print("Detalles de ventas por pelicula:")
        for k, v in peliculas_contador.items():
            print(f"- {k}: {v} boletos/ventas")
            print("Detalles de ventas por combo:")
            for k, v in combos_contador.items():
                print(f"- {k}: {v} unidades")
                print("=====================================================================")


def corte_de_caja ():


def main ():