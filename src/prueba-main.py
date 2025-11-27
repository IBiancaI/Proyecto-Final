import prueba_txt as fn
import csv

def main ():
    while True:
        mostrar_menu_principal()
        opcion = input("Opcion: ") .strip()

        if opcion == "1":
            registrar_ventas()
        elif opcion == "2":
            mostrar_resumen()
        elif opcion == "3":
            corte_de_caja()
        elif opcion == "4":
            print("Saliendo del programa. ¡Adios!")
            break
        else:
            print("Opcion no valida.")

if __name__ =="__main__":
    main()