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
    
combos_precios = {
    "palomitas con cocacola": 150.00,
    "palomitas y dos raspados": 170.00,
    "palomitas y nachos": 199.00
}
print("==============================================")
print("       BIENVENIDO AL CINE PYTHON")
print("==============================================")
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
            print("Entrada invalida. Ingresa un numero entero.")

def pedir_float (prompt, minimo = None):

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
    num_clientes = pedir_entero("¿Cuántos clientes se registrarán hoy? (0 para volver): ", minimo=0)
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
        pelicula = "Terrifier 3" 
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


def determinar_mas_vendido (contador_dict):
    max_val = -1
    winners = []
    for k, v in contador_dict.items():
        if v > max_val:
            max_val = v
            winners =  [k]
        elif v == max_val:
            winners.append(k)
    if max_val == 0:
        return None #NADA VENDIDO
    return winners if len(winners) > 1 else winners[0]  


def mostrar_resumen ():
   print("\n================================================")
   print("         R E S U M E N   D E L    D I A")
   print("================================================")
   peli_top = determinar_mas_vendido(peliculas_contador)
   combo_top = determinar_mas_vendido(combos_contador)

   if peli_top is None:
        print("Películas más vista: Ninguna venta aún.")
   else:
        if isinstance(peli_top, list):
            print("Películas más vistas (empatadas):", ", ".join([p.title() for p in peli_top]))
        else:
            print("Película más vista:", peli_top.replace("_", " ").title())

   if combo_top is None:
        print("Combo más vendido: Ninguno aún.")
   else:
        if isinstance(combo_top, list):
            print("Combos más vendidos (empatados):", ", ".join([c.replace("cocacola", "Coca-Cola").title() for c in combo_top]))
        else:
            print("Combo más vendido:", combo_top.replace("cocacola", "Coca-Cola").title())

   print("TOTAL DE VENTAS DEL DÍA: $", round(total_general, 2))
   print("\nDetalles de ventas por película:")
   for k, v in peliculas_contador.items():
        print(f"- {k.replace('_', ' ').title()}: {v} boletos/ventas")
   print("\nDetalles de ventas por combo:")
   for k, v in combos_contador.items():
        print(f"- {k.replace('cocacola', 'Coca-Cola').title()}: {v} unidades")
   print("=====================================================================")

def corte_de_caja ():
    print("\n---CORTE DE CAJA---")

    #Fecha del corte
    while True:
        fecha = input("Ingresa la fecha del corte (DD/MM/AAAA):").strip()
        if fecha != "":
            break

    print("\nIngreso de billetes:")
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

    total_caja = (b1000*1000 + b500*500 + b200*200 + b100*100 +
                  b50*50 + b20*20 + m10*10 + m5*5 + m2*2 +
                  m1*1 + m050*0.5)
    print("===========================================================================")
    print("TOTAL DE DINERO CONTADO: $", round(total_caja, 2))

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
        opcion = input("Opcion: ") .strip()

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

if __name__ =="__main__":
    main()