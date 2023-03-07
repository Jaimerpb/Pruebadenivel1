import helpers
import database as db



def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar los vehículos ")
        print("[2] Buscar un vehículo   ")
        print("[3] Añadir un vehículo   ")
        
        print("[4] Borrar un vehículo   ")
        print("[5] Catalogar por ruedas")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los vehiculos...\n")
            for vehiculo in db.Vehiculos.lista:
                print("{}: {}".format(type(vehiculo).__name__, vehiculo))
        
        elif opcion == '2':
            print("Buscando un vehículo...\n")
            numerodebastidor = helpers.leer_texto(3, 3, "numerodebastidor (2 int y 1 char)").upper()
            vehiculo = db.Vehiculos.buscar(id)
            print("{}: {}".format(type(vehiculo).__name__, vehiculo)) if vehiculo else print("Vehículo no encontrado.")

        elif opcion == '3':
            print("=======================")
            print(" Selección de Vehículo  ")
            print("=======================")
            print("[1] Coche")
            print("[2] Bicicleta   ")
            print("[3] Formula 1   ")
            print("[4] Camioneta")
            print("[5] Motocicleta   ")
            print("[6] Quad    ")
            print("=======================")

            opcion = input("> ")
            helpers.limpiar_pantalla()
            print("Añadiendo un vehículo...\n")

            numerodebastidor = None
            while True:
                numerodebastidor= helpers.leer_texto(3, 3, "Numero de bastidor (2 int y 1 char)").upper()
                if helpers.numerodebastidor_valido(numerodebastidor, db.Vehiculos.lista):
                    break

            color = helpers.leer_texto(2, 30, "Color").capitalize()
            ruedas = helpers.leer_numero(1, 30, "Ruedas (int)").capitalize()

            if opcion == '1':
                velocidad = helpers.leer_numero(1, 400, "Velocidad km/h (int)").capitalize()
                cilindrada = helpers.leer_numero(1, 2000, "Cilindrada cc (int)").capitalize()
                db.Vehiculos.crear(opcion, numerodebastidor, color, ruedas, velocidad, cilindrada)

            elif opcion == '2':
                tipo = helpers.leer_texto(1, 10, "Tipo (urbana/deportiva)").capitalize()
                db.Vehiculos.crear(opcion, numerodebastidor, color, ruedas, tipo)

            elif opcion == '3':
                velocidad = helpers.leer_numero(1, 400, "Velocidad km/h (int)").capitalize()
                cilindrada = helpers.leer_texto(1, 2000, "Cilindrada cc (int)").capitalize()
                equipo = helpers.leer_texto(1, 20, "Equipo").capitalize()
                db.Vehiculos.crear(opcion, numerodebastidor, color, ruedas, velocidad, cilindrada, equipo)

            elif opcion == '4':
                velocidad = helpers.leer_numero(1, 400, "Velocidad km/h (int)").capitalize()
                cilindrada = helpers.leer_texto(1, 2000, "Cilindrada cc (int)").capitalize()
                carga = helpers.leer_numero(1, 8000, "Carga kg (int)").capitalize()
                db.Vehiculos.crear(opcion, numerodebastidor, color, ruedas, velocidad, cilindrada, carga)

            elif opcion == '5':
                tipo = helpers.leer_texto(1, 10, "Tipo (urbana/deportiva)").capitalize()
                velocidad = helpers.leer_numero(1, 400, "Velocidad km/h (int)").capitalize()
                cilindrada = helpers.leer_texto(1, 2000, "Cilindrada cc (int)").capitalize()

            elif opcion == '6':
                velocidad = helpers.leer_numero(1, 400, "Velocidad km/h (int)").capitalize()
                cilindrada = helpers.leer_texto(1, 2000, "Cilindrada cc (int)").capitalize()
                tipo = helpers.leer_texto(1, 10, "Tipo (urbana/deportiva)").capitalize()
                modelo = helpers.leer_texto(1, 20, "Modelo").capitalize()
                carga = helpers.leer_numero(1, 8000, "Carga kg (int)").capitalize()
                db.Vehiculos.crear(opcion, numerodebastidor, color, ruedas, velocidad, cilindrada, tipo, modelo, carga)

            print("Vehículo añadido correctamente.")

        elif opcion == '4':
            print("Borrando un vehículo...\n")
            numerodebastidor = helpers.leer_texto(3, 3, "numerodebastidor (2 int y 1 char)").upper()
            print("Vehículo borrado correctamente.") if db.Vehiculos.borrar(
                numerodebastidor) else print("Vehículo no encontrado.")

        elif opcion == '5':
            print("Buscando por ruedas...\n")

            ruedas = input("Ruedas (1 int)\n> ")
            helpers.catalogar(db.Vehiculos.lista, ruedas)

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")