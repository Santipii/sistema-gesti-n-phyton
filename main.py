from entities.policlinica import Policlinica


if __name__ == "__main__":
    
    policlinica=Policlinica()
    print("-----------------------------------")
    print("Policlínica. Elija una opción.")
    while True:
        print("-----------------------------------")
        print("1 - Dar de alta una especialidad.")
        print("2 - Dar de alta un socio")
        print("3 - Dar de alta un médico.")
        print("4 - Dar de alta una consulta medica.")
        print("5 - Emitir un ticket de consulta.")
        print("6 - Realizar una consulta.")
        print("7 - Salir del programa.")
        print("-----------------------------------")
        
        opcion = policlinica.opcion(1, 7)

        print("-----------------------------------")

        if opcion == 1:
            policlinica.menu_especialidad()

        if opcion == 2:
            policlinica.menu_socio()

        if opcion == 3:
            policlinica.menu_medico()

        if opcion == 4:
            policlinica.menu_alta_consulta()

        if opcion == 5:
            policlinica.menu_emitir_ticket_consulta()

        if opcion == 6:
            policlinica.menu_consultas()

        if opcion == 7:
            quit()