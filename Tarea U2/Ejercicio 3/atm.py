class Atm:
    saldo = 2000        # cuenta de vacaciones clienete 1
    saldo2 = 1000       # cuenta de vacaciones cliente 2
    cuentaAhorro1 = 400 # cuenta de ahorro clinete 1
    cuentaAhorro2 = 300 # cuenta de ahorro cliente 2
    saldo_nuevo=0       
    
    print("\t BIENVENIDO A SU CAJERO AUTOMATICO")
    def operaciones(self):
        self.opcion = int(input('''
        ************************************
        INGRESE QUE OPERACION DESEA REALIZAR: 
        1. SELECCIONAR USUARIO 
        2. SELECCIONAR TIPO DE CUENTA
        3. CONSULTAR SALDO                           
        4. AGREGAR SALDO
        5. RETIRO                       
        6. CREAR CUENTA NUEVA
        7. SALIR'''))
        self.control=0
        while self.control == 0:
            if self.opcion == 1:
                self.usuario_cliente()
            elif self.opcion == 2:
                self.seleccionar_cuenta()
            elif self.opcion == 3:
                self.consulta_saldo()
            elif self.opcion == 4:
                self.agregar_saldo()
            elif self.opcion == 5:
                self.retirar()
            elif self.opcion == 6:
                self.crear_cuentaNueva()
            elif self.opcion == 7:
                self.control = 1
                self.salir()
            else:
                print("OPCION NO VALIDA, INTENTE DE NUEVO: ")
                self.operaciones()

    def consulta_saldo(self):
        tipo_cuenta = int(input('''CONSULTAR SALDO EN: 
        ******************************
                                1. CUENTA DE AHORRO DE MIGUEL
                                2. CUENTA DE VACACIONES DE MIGUEL
                                3. CUENTA DE AHORRO DE RUBEN
                                4. CUENTA DE VACACIONES DE RUBEN'''))
        if tipo_cuenta == 1:
            print("EL SALDO DISPONIBLE EN SU CUENTA DE AHORRO ES: ", self.cuentaAhorro1)
            print("EL SALDO TOTAL DE LAS CUENTAS DE MIGUEL ES: ", self.cuentaAhorro1 + self.saldo)
        elif tipo_cuenta == 2:
            print("EL SALDO DISPONIBLE EN SU CUENTA DE VACACIONES ES: ", self.saldo)
            print("EL SALDO TOTAL DE LAS CUENTAS DE MIGUEL ES: ", self.cuentaAhorro1 + self.saldo)
        elif tipo_cuenta == 3:
            print("EL SALDO DISPONIBLE EN SU CUENTA DE AHORRO ES: ", self.cuentaAhorro2)
            print("EL SALDO TOTAL DISPONIBLE EN LAS CUENTAS DE RUBEN ES: ", self.cuentaAhorro2 + self.saldo2)
        elif tipo_cuenta == 4:
            print("EL SALDO DISPONIBLE EN SU CUENTA DE VACACIONES ES: ", self.saldo2)
            print("EL SALDO TOTAL DISPONIBLE EN LAS CUENTAS DE RUBEN ES: ", self.cuentaAhorro2 + self.saldo2)
        else:
            print("OPCION DE CUENTA NO DISPONIBLE")  
        print("¿QUIERE REALIZAR OTRA OPERACION?")
        self.operaciones()

    def agregar_saldo(self):
        elegir = int(input('''Selecciona la cuenta que deseas
                            1. CUENTA DE AHORRO DE MIGUEL
                            2. CUENTA DE VACACIONES DE MIGUEL
                            3. CUENTA DE AHORRO DE RUBEN
                            4. CUENTA DE VACACIONES DE RUBEN '''))
        if elegir == 1:
            print("Seleccionaste la cuenta de ahorro de miguel")
            self.deposito = int(input("INGRESE LA CANTIDAD A AGREGAR: "))
            self.cuentaAhorro1=self.cuentaAhorro1 + self.deposito
            self.consulta_saldo()
        
        elif elegir == 2:
            print("Seleccionaste la cuenta de vacaciones de miguel")
            self.deposito = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
            self.saldo = self.saldo + self.deposito
            self.consulta_saldo()
        elif elegir ==3:
            print("seleccionaste la cuenta de ahorro de ruben")
            self.deposito = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
            self.cuentaAhorro2 = self.cuentaAhorro2 + self.deposito
            self.consulta_saldo
        elif elegir ==4:
            print("seleccionaste la cuenta de vacaciones de ruben")
            self.deposito = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
            self.saldo2 = self.saldo2 + self.deposito
            self.consulta_saldo
        else:
            print("Opcion invalida, selecciones otra")
            self.agregar_saldo()

    def retirar(self): 
        
        seleccion = int(input('''Selecciona la cuenta que deseas
                            1. CUENTA DE AHORRO DE MIGUEL
                            2. CUENTA DE VACACIONES DE MIGUEL
                            3. CUENTA DE AHORRO DE RUBEN
                            4. CUENTA DE VACACIONES DE RUBEN '''))
        if seleccion == 1:
            print("seleccionaste la cuenta de ahorro de miguel")
            self.retiro = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
            self.cuentaAhorro1 = self.cuentaAhorro1 - self.retiro
            if self.retiro > self.cuentaAhorro1:
                print('''LA CANTIDAD INGRESADA SOBREPASA SU SALDO, INGRESE OTRA:
                ********************************''')
                self.retiro = int(input("INDIQUE LA CANTIDAD A RETIRAR: "))
            self.consulta_saldo()
            
        elif seleccion == 2:
            print("Seleccionaste la cuenta de vacaciones de miguel")
            self.retiro = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
            self.saldo = self.saldo - self.retiro
            if self.retiro > self.saldo:
                print('''LA CANTIDAD INGRESADA SOBREPASA SU SALDO, INGRESE OTRA:
                ********************************''')
                self.retiro = int(input("INDIQUE LA CANTIDAD A RETIRAR: ")) 
            self.consulta_saldo()
        elif seleccion == 3:
            print("Seleccionaste la cuenta de ahorro de ruben")
            self.retiro = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
            self.cuentaAhorro2 = self.cuentaAhorro2 - self.retiro
            if self.retiro > self.cuentaAhorro2:
                print('''LA CANTIDAD INGRESADA SOBREPASA SU SALDO, INGRESE OTRA:
                ********************************''')
                self.retiro = int(input("INDIQUE LA CANTIDAD A RETIRAR: "))
            self.consulta_saldo()
        elif seleccion == 4:
            print("Seleccionaste la cuenta de vacaciones de ruben")
            self.retiro = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
            self.saldo2 = self.saldo2 - self.retiro
            if self.retiro > self.saldo2:
                print('''LA CANTIDAD INGRESADA SOBREPASA SU SALDO, INGRESE OTRA:
                ********************************''')
                self.retiro = int(input("INDIQUE LA CANTIDAD A RETIRAR: "))
            self.consulta_saldo()
        else:
            print("Opcion invalida, selecciones otra")
            self.retirar() # ya esta correcto con esto 

    def salir(self):
        print("*************************")
        print(" \t GRACIAS!")
        print("*************************")

    def crear_cuentaNueva(self):
        self.nombre = input("INGRESE UN NOMBRE IDENTIFICADOR: ")
        print("SU NOMBRE IDENTIFICADOR ES:", self.nombre)
        self.saldo_nuevo = float(input("INGRESE UN SALDO INICIAL: "))
        print("SU SALDO INICIAL EN SU NUEVA CUENTA ES: ", self.saldo_nuevo)
        print("NUEVA CUENTA CREADA CON EXITO!")
        self.operaciones()

    def seleccionar_cuenta(self):
        cuenta = int(input('''SELECCIONA EL TIPO DE CUENTA:
        *********************************
                        1. AHORRO
                        2. VACACIONES'''))
        if cuenta == 1:
            print("SELECCIONASTE TU CUENTA DE AHORRO")
            self.operaciones()
        elif cuenta == 2:
            print("SELECCIONASTE TU CUENTA DE VACACIONES")
            self.operaciones()
        else:
            print("OPCION NO VALIDA, INGRESA OTRA")
            self.seleccionar_cuenta()

    def usuario_cliente(self):
        usuario = int(input('''SELECCIONAR CLIENTE:
        *******************************
                            1. MIGUEL
                            2. RUBEN'''))
        if usuario == 1:
            print("CUENTA DE MIGUEL")
            print("Sus cuentas son: ", " Cuenta de vacaciones: ", self.saldo, "y cuenta de ahorro: ", self.cuentaAhorro1)
            self.operaciones()
        elif usuario == 2:
            print("CUENTA DE RUBEN")
            print("Sus cuentas son: ", "Cuenta vacaciones: ", self.saldo2, "y cuenta de ahorro: ", self.cuentaAhorro2) 
            self.operaciones()
        else:
            print("OPCION NO VALIDA, INGRESA OTRA")
            self.usuario_cliente()

# objeto
mi_cajero = Atm()
mi_cajero.operaciones()

