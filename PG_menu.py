import tkinter as tk
import helpers
import menu
class MenuGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Bienvenido al Gestor")
        self.label.pack(side="top")

        self.listar_button = tk.Button(self, text="Listar los vehículos", command=self.listar_vehiculos)
        self.listar_button.pack()

        self.buscar_button = tk.Button(self, text="Buscar un vehículo", command=self.buscar_vehiculo)
        self.buscar_button.pack()

        self.aniadir_button = tk.Button(self, text="Añadir un vehículo", command=self.anadir_vehiculo)
        self.aniadir_button.pack()

        self.borrar_button = tk.Button(self, text="Borrar un vehículo", command=self.borrar_vehiculo)
        self.borrar_button.pack()

        self.catalogar_button = tk.Button(self, text="Catalogar por ruedas", command=self.catalogar_vehiculos)
        self.catalogar_button.pack()

        self.cerrar_button = tk.Button(self, text="Cerrar el Gestor", command=self.master.quit)
        self.cerrar_button.pack()

    def listar_vehiculos(self):
        helpers.limpiar_pantalla()
        print("Listando los vehículos...\n")
        for vehiculo in db.Vehiculos.lista:
            print("{}: {}".format(type(vehiculo).__name__, vehiculo))

    def buscar_vehiculo(self):
        helpers.limpiar_pantalla()
        print("Buscando un vehículo...\n")
        id = helpers.leer_texto(3, 3, "Numero de bastidor (2 int y 1 char)").upper()
        vehiculo = db.Vehiculos.buscar(numerodebastidor)
        print("{}: {}".format(type(vehiculo).__name__, vehiculo)) if vehiculo else print("Vehículo no encontrado.")

    def anadir_vehiculo(self):
        helpers.limpiar_pantalla()
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

        id = None
        while True:
            id = helpers.leer_texto(3, 3, "Numero de bastidor (2 int y 1 char)").upper()
            if helpers.numerodebastidor_valido(numerodebastidor, db.Vehiculos.lista):
                break

        color = helpers.leer_texto(2, 30, "Color").capitalize()
        ruedas = helpers.leer_numero(1, 30, "Ruedas (int)").capitalize()

        if opcion == '1':
            velocidad = helpers.leer_numero ("Velocidad km/h")
            cilindrada = helpers.leer_numero("Cilindrada (cc)")
            db.Vehiculos.lista.append(db.Coche(numerodebastidor, color, ruedas, velocidad, cilindrada))
        if opcion == '2':
            tipo == helpers.leer_texto("Tipo(urbana,deportiva)")
            db.Vehiculos.lista.append(db.Bicicleta(numerodebastidor, color, ruedas, tipo))
        if opcion == '3':
            velocidad = helpers.leer_numero ("Velocidad km/h")
            cilindrada = helpers.leer_numero("Cilindrada (cc)")
            carga = helpers.leer_numero("Carga (kg)")
            equipo= helpers.leer_texto("Equipo")
            db.Vehiculos.lista.append(db.Formula1(numerodebastidor, color, ruedas, velocidad, cilindrada, carga, equipo))
        if opcion == '4':
            velocidad = helpers.leer_numero ("Velocidad km/h")
            cilindrada = helpers.leer_numero("Cilindrada (cc)")
            carga = helpers.leer_numero("Carga (kg)")
            db.Vehiculos.lista.append(db.Camioneta(numerodebastidor, color, ruedas, velocidad, cilindrada, carga))
        if opcion == '5':
            velocidad = helpers.leer_numero ("Velocidad km/h")
            cilindrada = helpers.leer_numero("Cilindrada (cc)")
            tipo= helpers.leer_texto("Tipo(urbana,deportiva)")
            db.Vehiculos.lista.append(db.Motocicleta(numerodebastidor, color, ruedas, velocidad, cilindrada, tipo))
        if opcion == '6':
            velocidad = helpers.leer_numero ("Velocidad km/h")
            cilindrada = helpers.leer_numero("Cilindrada (cc)")
            tipo= helpers.leer_texto("Tipo(urbana,deportiva)")
            modelo= helpers.leer_texto("Modelo")
            db.Vehiculos.lista.append(db.Quad(numerodebastidor, color, ruedas, velocidad, cilindrada, tipo, modelo))

