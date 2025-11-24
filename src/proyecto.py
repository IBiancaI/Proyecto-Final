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

def pedir_float ():


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


def determinar_mas_vendido (contador_dict):
    max_val= -1
    winners=[]
    for k,v in contador_dict.items():
        if v > max_val:
            max_val = v 
            winners = [k]
        elif v == max_val:
            winners.append(k)
    if max_val == 0:
        return None
    return winners if len (winners) > 1 else winners[0]




def mostrar_resumen ():


def corte_de_caja ():


def main ():