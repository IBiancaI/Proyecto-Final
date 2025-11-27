import prueba_txt as fn
import csv

def main ():
    combos_precios = []
    archivo = input("Ingrese el nombre del archivo de ventas: ")
    ventas = fn.leer_archivo(archivo,combos_precios)
    while True:
    
        opcion = fn.mostrar_menu_principal()

        if opcion == "1":
            combos_precios = fn.registrar_ventas()
        elif opcion == "2":
            combos_precios = fn.mostrar_resumen()
        elif opcion == "3":
            combos_precios = fn.corte_de_caja()
        elif opcion == "4":
            print("Saliendo del programa. ¡Adios!")
            break
        else:
            print("Opcion no valida.")

if __name__ =="__main__":
    main()