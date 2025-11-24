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
    
precios_combo = {
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

def pedir_float ():


def mostrar_menu_principal():
    print("\n---MENU PRINCIPAL---")
    print("1. Registrar ventas")
    print("2. Ver resumen del dia")
    print("3. Corte de caja")
    print("4. Salir")





def resistrar_ventas ():


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
    print("\n---CORTE DE CAJA---")

    #Fecha del corte
    fecha = ""
    while not fecha:
        fecha = input("Ingresa la fecha del corte (DD/MM/AAAA):").strip()

print("\nBilletes:")
b1000 = pedir_entero("$1000: ", minimo=0)
b500  = pedir_entero("$500: ", minimo=0)
b200 = pedir_entero("$200:", minimo=0)
b100 = pedir_entero("$100:", minimo=0)
b50 = pedir_entero("$50:", minimo=0)
b20 = pedir_entero("$20:", minimo=0)



def main ():
    while True:
        mostrar_menu_principal()
        opcion = input("Opcion: ") .strip()

        if opcion == 1:
            resistrar_ventas()
        elif opcion == 2:
            mostrar_resumen()
        elif opcion == 3:
            corte_de_caja()
        elif opcion == 4:
            print("Saliendo del programa. ¡Adios!")
            break
        else:
            print("Opcion no valida.")