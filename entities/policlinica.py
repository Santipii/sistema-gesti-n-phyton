from entities.especialidad import Especialidad
from entities.medico import Medico
from entities.socio import Socio
from entities.consulta import Consulta
from exceptions.EntidadYaExiste import EntidadYaExiste
from datetime import datetime


class Policlinica:
    def __init__(self):
        self.__lista_especialidades = []
        self.__lista_socios = []
        self.__lista_medicos = []
        self.__lista_consultas = []

    @property
    def lista_especialidades(self):
        return self.__lista_especialidades

    @property
    def lista_socios(self):
        return self.__lista_socios

    @property
    def lista_medicos(self):
        return self.__lista_medicos
    
    @property
    def lista_consultas(self):
        return self.__lista_consultas

    # Funciones para conseguir inputs y dos fechas.

    def conseguir_input(self, pregunta, condicion, error):
        while True:
            respuesta = input(pregunta)
            if condicion(respuesta):
                return respuesta
            else:
                print(error)
                continue

    def conseguir_fechas(self):
        fecha_inicio = self.conseguir_input("Ingrese la fecha de inicio en formato aaaa-mm-dd: ", 
                                            self.verificar_fecha, 
                                            "No es una fecha válida. Vuelva a ingresarla en el formato aaaa-mm-dd.")
        
        fecha_final = self.conseguir_input("Ingrese la fecha final en formato aaaa-mm-dd: ", 
                                            self.verificar_fecha, 
                                            "No es una fecha válida. Vuelva a ingresarla en el formato aaaa-mm-dd.")
        
        return fecha_inicio, fecha_final

    # Verificaciones de inputs.           

    def verificar_fecha(self, fecha_str):
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    def verificar_string(self, string):
        if isinstance(string, str):
            if string != "":
                if not any(caracteres.isdigit() for caracteres in string):
                    return True
        return False
    
    def verificar_entero(self, numero):
        try:
            numero_int = int(numero)
            if numero_int < 0: # Nunca trabajamos con números negativos así que esto no causará problemas. Probablemente.
                return False
            return True
        
        except ValueError:
            return False      

    # Verificaciones de clase. 
        
    def verificar_socio(self, socio_ci):
        for socios in self.__lista_socios:
            if socios.ci == socio_ci:
                return socios
        return None

    def verificar_especialidad(self, especialidad_nombre):
        for especialidades in self.__lista_especialidades:
            if especialidades.nombre == especialidad_nombre:
                return especialidades
        return None
    
    def verificar_medico(self, medico_nombre, medico_apellido):
        for medicos in self.__lista_medicos:
            if medicos.nombre == medico_nombre and medicos.apellido == medico_apellido:
                return medicos
        return None
    
    # Altas.
    
    def alta_especialidad(self, especialidad, precio):
        if self.verificar_especialidad(especialidad) != None:
            raise EntidadYaExiste("La especialidad ya está registrada.")
        
        nueva_especialidad = Especialidad(especialidad, precio)
        self.__lista_especialidades.append(nueva_especialidad)

    def alta_socio(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo):
        if self.verificar_socio(ci) != None:
            raise EntidadYaExiste("El socio ya está registrado.")

        nuevo_socio = Socio(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo)
        self.__lista_socios.append(nuevo_socio)

    def alta_medico(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, especialidad_medico):
        if self.verificar_medico(nombre, apellido) != None:
            raise EntidadYaExiste("El médico ya está registrado.")

        nuevo_medico = Medico(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, especialidad_medico)
        self.__lista_medicos.append(nuevo_medico)

    def alta_consulta(self, especialidad, medico, fecha_consulta, pacientes):
        nueva_consulta = Consulta(especialidad, medico, fecha_consulta, pacientes)
        self.__lista_consultas.append(nueva_consulta)

    # Función para conseguir una persona. Será usada en socio y médico.    

    def conseguir_persona(self):
        nombre = self.conseguir_input("Ingrese el nombre: ", 
                                     self.verificar_string, 
                                     "No es un nombre válido. Ingréselo de nuevo.")
                
        apellido = self.conseguir_input("Ingrese el apellido: ", 
                                        self.verificar_string, 
                                        "No es un apellido válido. Ingréselo de nuevo.")
                
        ci = self.conseguir_input("Ingrese la cédula de identidad: ", 
                                 lambda x: len(x) == 8 and self.verificar_entero(x),
                                 "No es una cédula válida. Ingrese nuevamente una cédula de 8 dígitos.")
                
        fecha_nacimiento = self.conseguir_input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ", 
                                                self.verificar_fecha, 
                                                "No es una fecha válida. Vuelva a ingresarla en el formato aaaa-mm-dd.")
                
        fecha_ingreso = self.conseguir_input("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ",
                                            self.verificar_fecha, 
                                            "No es una fecha válida. Vuelva a ingresarla en el formato aaaa-mm-dd.")
                
        celular = self.conseguir_input("Ingrese el número de celular: ", 
                                      lambda x: len(x) == 9 and x.startswith("09") and self.verificar_entero(x), 
                                      "No es un número de celular válido. Ingrese un número con el formato 09XXXXXXXX.")
        
        return nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular

    # Menús.
        
    def menu_especialidad(self):
        while True:
            
            nombre = self.conseguir_input("Ingrese el nombre de la especialidad: ",
                                           self.verificar_string,
                                            "No es un nombre válido. Ingréselo de nuevo.")

            precio = self.conseguir_input("Ingrese el precio asociado: ",
                                           self.verificar_entero,
                                            "No es un precio válido. Ingréselo de nuevo.")
            
            precio = int(precio) # Tras verificar que se puede convertir en entero, lo hace.

            try:
                self.alta_especialidad(nombre, precio)
                print("La especialidad se ha dado de alta exitosamente.")
                break
            except EntidadYaExiste as e:
                print(e)
                break

    def submenu_especialidad(self):
        while True:
            especialidad = self.conseguir_input("Ingrese la especialidad: ",
                                                self.verificar_string,
                                                "Especialidad inválida. Ingrésela de nuevo.")
            
            especialidad_verificada = self.verificar_especialidad(especialidad)
            if especialidad_verificada == None:
                opcion = self.conseguir_input("La especialidad no está registrada.\n1 - Volver a ingresar la especialidad.\n2 - Dar de alta esta especialidad.\n",
                                                lambda x: x in ["1", "2"],
                                                "Opción inválida.")
                if opcion == "1":
                    continue
                            
                elif opcion == "2":
                    self.menu_especialidad()
                    return self.verificar_especialidad(especialidad)
                
            else:
                return especialidad_verificada
                

    def menu_socio(self):
        while True:
            nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular = self.conseguir_persona()

            tipo = self.conseguir_input("Establezca el tipo de socio:\n1 - Bonificado.\n2 - No bonificado.\nOpción: ",
                                        lambda x: x in ["1", "2"],
                                        "Número inválido.")
            
            try:
                self.alta_socio(nombre, 
                                apellido, 
                                ci, 
                                fecha_nacimiento, 
                                fecha_ingreso, 
                                celular, 
                                tipo)
                
                print("Socio dado de alta exitosamente.")
                break

            except EntidadYaExiste as e:
                print(e)
                break

    def submenu_socio(self):
        while True:
            socio = self.conseguir_input("Ingrese la cédula del socio: ",
                                          lambda x: self.verificar_entero(x) and len(x) == 8,
                                          "Cédula inválida. Ingrésela de nuevo.") 
                 
            socio_verificado = self.verificar_socio(socio)
            if socio_verificado == None:
                opcion = self.conseguir_input("El socio no está registrado.\n1 - Volver a ingresar al socio.\n2 - Dar de alta al socio.\nOpción: ",
                                            lambda x: x in ["1", "2"],
                                            "Opción inválida.")
                if opcion == "1":
                    continue
                            
                elif opcion == "2":
                    print()
                    self.menu_socio()
                    return self.verificar_socio(socio)
            
            else:
                return socio_verificado

    def menu_medico(self):
        while True:
            nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular = self.conseguir_persona()
            especialidad = self.submenu_especialidad()

            try:
                self.alta_medico(nombre, 
                                apellido, 
                                ci, 
                                fecha_nacimiento, 
                                fecha_ingreso, 
                                celular, 
                                especialidad)
                print("Médico dado de alta exitosamente.")
                break
            except EntidadYaExiste as e:
                print(e)
                break        

    def submenu_medico(self):
        while True:
            medico = self.conseguir_input("Ingrese el nombre y apellido del médico: ",
                                          self.verificar_string,
                                          "Médico inválido. Ingréselo de nuevo.")
            
            nombre, apellido = medico.split()
                  
            if self.verificar_medico(nombre, apellido) == None:
                opcion = self.conseguir_input("El médico no está registrado.\n1 - Volver a ingresar al médico.\n2 - Dar de alta al médico.\nOpción: ",
                                            lambda x: x in ["1", "2"],
                                            "Opción inválida.")
                if opcion == "1":
                    continue
                            
                elif opcion == "2":
                    print()
                    self.menu_medico()
                    return self.verificar_medico(nombre, apellido)
            else:
                return self.verificar_medico(nombre, apellido)
                
                
    def menu_alta_consulta(self):
        consulta_especialidad = self.submenu_especialidad()
        consulta_medico = self.submenu_medico()
        consulta_fecha = self.conseguir_input("Ingrese la fecha de consulta en formato aaaa-mm-dd: ",
                                                self.verificar_fecha,
                                                "No es una fecha válida. Vuelva a ingresarla en el formato aaaa-mm-dd.")
            
        consulta_pacientes = self.conseguir_input("Ingrese el número de pacientes: ",
                                                    self.verificar_entero,
                                                    "Número inválido. Ingréselo de nuevo.")
        
        consulta_pacientes = list(range(1, int(consulta_pacientes) + 1)) # Escalofriante línea de código. 

        print("Consulta dada de alta exitosamente.")
        self.alta_consulta(consulta_especialidad, consulta_medico, consulta_fecha, consulta_pacientes)

    def menu_emitir_ticket_consulta(self):
        especialidad = self.submenu_especialidad()
        consultas_especialidad = [consultas for consultas in self.__lista_consultas if consultas.especialidad == especialidad]
        if not consultas_especialidad:
            print("No hay consultas disponibles para esta especialidad.")
            return
        else:
            print(f"Consultas para {especialidad.nombre}:")
        for i, consultas in enumerate(consultas_especialidad):
            print(f"{i+1}: Doctor: {consultas.medico.nombre} {consultas.medico.apellido} | Día de la consulta: {consultas.fecha}")

        opcion = self.conseguir_input("Seleccionar la consulta deseada: ",
                                      lambda x: self.verificar_entero(x) and 1 <= int(x) <= len(consultas_especialidad),
                                      "Consulta inválida.")
        
        opcion = int(opcion)
        
        consulta_seleccionada = consultas_especialidad[opcion-1]
        if not consulta_seleccionada.pacientes:
            print("No hay más tickets disponibles para esta consulta.")
            return
        else:
            print(f"Números disponibles: {consulta_seleccionada.pacientes}")

            opcion2 = self.conseguir_input("Seleccionar el número de atención deseado: ",
                                          lambda x: self.verificar_entero(x) and 1 <= int(x) <= len(consulta_seleccionada.pacientes),
                                          "Número de atención inválido.")
            
            opcion2 = int(opcion2)

            socio = self.submenu_socio()

            consulta_seleccionada.borrar_paciente(opcion2)
            socio.deuda += especialidad.precio

            if socio.tipo == "1":
                consulta_seleccionada.tickets = 0.8
            else:
                consulta_seleccionada.tickets = 1

            print(f"Ticket emitido a nombre de {socio.nombre} {socio.apellido}.")

    def opcion(self, n1, n2):
        while True:
            try:
                opcion = int(input("Opción: "))
                if opcion in range(n1, n2 + 1):
                    return opcion
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Opción inválida.")
                continue

    # Realizar consultas.
    
    def consultas_doctores_especialidad(self):
        especialidad = self.submenu_especialidad()
        matriz_medicos = [medicos for medicos in self.__lista_medicos if medicos.especialidad == especialidad]
        if not matriz_medicos:
            print("No hay médicos asociados a esta especialidad.")
        else:
            print(f"Médicos asociados a {especialidad.nombre}:")
            for i, medicos in enumerate(matriz_medicos):
                print(f"{i+1}: {medicos.nombre} {medicos.apellido}")
            
    def consultas_precio_especialidad(self):
        especialidad = self.submenu_especialidad()
        print(f"El precio de consulta para {especialidad.nombre} es {especialidad.precio}$.")

    def consultas_socios(self):
        matriz_socios = [socios for socios in self.__lista_socios]
        matriz_socios.sort(key = lambda x: x.deuda)

        if not matriz_socios:
            print("No hay ningún socio registrado.")
        else:
            print("Lista de socios:")
            for i, socios_sorteados in enumerate(matriz_socios):
                    print(f"{i+1}: {socios_sorteados.nombre} {socios_sorteados.apellido} | Deuda: {socios_sorteados.deuda}")  

    def consultar_consultas(self): # Nombre completamente intencional.
        fecha_inicio, fecha_final = self.conseguir_fechas()

        matriz_consultas = [consultas for consultas in self.__lista_consultas if fecha_inicio <= consultas.fecha <= fecha_final]
        matriz_consultas.sort(key = lambda x: x.fecha)
        
        if not matriz_consultas:
            print("No hay consultas registradas dentro de ese rango de fechas.")
        else:
            print(f"Lista de consultas desde {fecha_inicio} hasta {fecha_final}:")
            for i, consultas in enumerate(matriz_consultas):
                print(f"{i+1}: Doctor: {consultas.medico.nombre} {consultas.medico.apellido} | Especialidad: {consultas.especialidad.nombre} | Fecha: {consultas.fecha} | Cant. Pacientes: {consultas.cant_pacientes}")

    def consultar_ganancias(self):
        fecha_inicio, fecha_final = self.conseguir_fechas()
        total_tickets = 0
        total_precio = 0

        for consultas in self.__lista_consultas:
            if fecha_inicio <= consultas.fecha <= fecha_final:
                if consultas.tickets != 0:
                    total_tickets += consultas.tickets
                    total_precio += consultas.especialidad.precio

        print(f"Las ganancias desde {fecha_inicio} hasta {fecha_final} han sido de {total_tickets * total_precio}$.")

    def menu_consultas(self):
        print("1. Obtener todos los médicos asociados a una especialidad específica.")
        print("2. Obtener el precio de una consulta de una especialidad en específico.")
        print("3. Listar todos los socios con sus deudas asociadas en orden ascendente.")
        print("4. Realizar consultas respecto a cantidad de consultas entre dos fechas.")
        print("5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.")
        opcion = self.opcion(1, 5)
        if opcion == 1:
            self.consultas_doctores_especialidad()
        if opcion == 2:
            self.consultas_precio_especialidad()
        if opcion == 3:
            self.consultas_socios()
        if opcion == 4:
            self.consultar_consultas()
        if opcion == 5:
            self.consultar_ganancias()
