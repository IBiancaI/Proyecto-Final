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