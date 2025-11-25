    # ---PROYECTO FINAL---

#Contadores de peliculas
total_general = 0
peliculas_contador = {
    "spiderman": 0,
    "terrifier 3": 0,
    "pac_man": 0
}
#Contadores de combos y precios
combos_contador = {c: 0 for c in ["palomitas con cocacola", "palomitas y dos raspados", "palomitas y nachos"]}
    
combos_pecios = {
    "palomitas con cocacola": 150.00,
    "palomitas y dos raspados": 170.00,
    "palomitas y nachos": 199.00
}

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
    #""""Pide un número (float) con validación y devuelve el valor."""
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
    print("\n---MENU PRINCIPAL---")
    print("1. Registrar ventas")
    print("2. Ver resumen del dia")
    print("3. Corte de caja")
    print("4. Salir")





def registrar_ventas ():
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
    #Selección de pelis
        pelicula_op = input ("Elige una película (1-3): ").strip()
    try:
        if pelicula_op == "1":
            pelicula = "spiderman"
        elif pelicula_op == "2":
            pelicula = "Terrifier 3"
        elif pelicula_op == "3":
            pelicula = "PacMan"
        else:
            print ("Número inválido")

    except ValueError:
        print("Entrafa invalida. Ingresa un numero entero.")

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
    max_val = -1
    winners = []
    for k, v in contador_dict.items():
        if v > max__val:
            max_val = v
            winners =  [k]
        elif v == max_val:
            winners.append(k)
    if max_val == 0:
        return None #NADA VENDIDO
    return winners if len(winners) > 1 else winners[0]  


def mostrar_resumen ():
    #""""Muestra un resumen sencillo del día.""""
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
    print("\n---CORTE DE CAJA---")

    #Fecha del corte
    while True:
        if fecha != "":
            fecha = input("Ingresa la fecha del corte (DD/MM/AAAA):").strip()
            break

#----------INGRESAMOS LAS BILLETES AQUI----------
    print("\n-------------------------------")
    print("\nIngreso de billetes")
    print("\n-------------------------------")
    b1000 = pedir_entero("$1000: ", minimo=0)
    b500  = pedir_entero("$500: ", minimo=0)
    b200 = pedir_entero("$200:", minimo=0)
    b100 = pedir_entero("$100:", minimo=0)
    b50 = pedir_entero("$50:", minimo=0)
    b20 = pedir_entero("$20:", minimo=0)

#----------INGRESAMOS LAS MONEDAS AQUI----------
    print("\n-------------------------------")
    print("        INGRESO DE MONEDAS       ")
    print("\n-------------------------------")
    m10 = pedir_entero("Monedas de $10:",minimo=0)
    m5 = pedir_entero("Monedas de $5:",minimo=0)
    m2 = pedir_entero("Monedas de $2:",minimo=0)
    m1 = pedir_entero("Monedas de $1:",minimo=0)
    m050 = pedir_entero("Monedas de $0.50:",minimo=0)

    #-------CODIGO FONDO---------
    while True:
        fondo = pedir_float("¿Cuanto deseas dejar de fondo en caja?")
        if fondo > total_caja:
            print("Erorr: No puedes dejar mas dinero del que tienes en caja. Intenta de nuevo.")
        else:
            break
    sobre = total_caja - fondo
    #----FONDOTOTAL------
    print("\n--------------------------------------------------")
    print("\nDINERO CONTADO: $",round(total_caja,2))
    print("\nDINERO PARA FONDO: $",round(fondo,2))     
    print("\nDINERO PARA SOBRE: $",round(sobre,2))
    print("\nFECHA DEL CORTE: $",round(fecha,2))
    print("\n--------------------------------------------------")
    print("CORTE FINALIZADO CORRECTAMENTE")

def main ():
    while True:
        mostrar_menu_principal()
        opcion = input("Opcion: ").strip()

        if opcion == 1:
            registrar_ventas()
        elif opcion == 2:
            mostrar_resumen()
        elif opcion == 3:
            corte_de_caja()
        elif opcion == 4:
            print("Saliendo del programa. ¡Adios!")
            break
        else:
            print("Opcion no valida.")