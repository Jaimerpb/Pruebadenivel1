import csv
import config

class Vehiculo():
    def __init__(self, númerodebastidor, color, ruedas):
        self.númerodebastidor= númerodebastidor
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "número de bastidor {}, color {}, {} ruedas".format(self.númerodebastidor, self.color, self.ruedas)
    
class Coche(Vehiculo):
    def __init__(self, númerodebastidor, color, ruedas, velocidad, cilindrada):
        super().__init__(númerodebastidor, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

class Bicicleta(Vehiculo):
    def __init__(self, númerodebastidor, color, ruedas, tipo):
        super().__init__(númerodebastidor, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + ", de tipo {}".format(self.tipo)

class Formula1(Coche):
    def __init__(self, númerodebastidor, color, ruedas, velocidad, cilindrada, equipo):
        super().__init__(númerodebastidor, color, ruedas, velocidad, cilindrada)
        self.equipo = equipo
    def __str__(self):
        return Coche.__str__(self) + ", del equipo {}".format(self.equipo)
    
class Camioneta(Coche):
    def __init__(self, númerodebastidor, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(númerodebastidor, color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return Coche.__str__(self) + ", {} kg de carga".format(self.carga)
    
class Motocicleta(Bicicleta):
    def __init__(self,númerodebastidor, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(númerodebastidor, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

class Quad(Coche):
    def __init__(self, númerodebastidor, color, ruedas, velocidad, cilindrada, tipo, modelo, carga):
        super().__init__(númerodebastidor, color, ruedas, velocidad, cilindrada)
        self.tipo = tipo
        self.modelo = modelo
        self.carga = carga
    def __str__(self):
        return Coche.__str__(self) + ", de tipo {}, modelo {}, {} kg de carga".format(self.tipo, self.modelo, self.carga)

class Vehiculos:
    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for tipo in reader:
            if tipo[0] == "Coche":
                coche = Coche(*tipo[1:])
                lista.append(coche)
            if tipo[0] == "Bicicleta":
                bicicleta = Bicicleta(*tipo[1:])
                lista.append(bicicleta)
            if tipo[0] == "Formula1":
                formula1 = Formula1(*tipo[1:])
                lista.append(formula1)
            if tipo[0] == "Camioneta":
                camioneta = Camioneta(*tipo[1:])
                lista.append(camioneta)
            if tipo[0] == "Motocicleta":
                motocicleta = Motocicleta(*tipo[1:])
                lista.append(motocicleta)
            if tipo[0] == "Quad":
                quad = Quad(*tipo[1:])
                lista.append(quad)

    @staticmethod
    def buscar(numerodebastidor):
        for vehiculo in Vehiculos.lista:
            if vehiculo.numerodebastidor == numerodebastidor:
                return vehiculo

    @staticmethod
    def crear(opcion, *args):
        if opcion == "1":
            vehiculo = Coche(*args)
        elif opcion == "2":
            vehiculo = Bicicleta(*args)
        elif opcion == "3":
            vehiculo = Formula1(*args)
        elif opcion == "4":
            vehiculo = Camioneta(*args)
        elif opcion == "5":
            vehiculo = Motocicleta(*args)
        elif opcion == "6":
            vehiculo = Quad(*args)
        Vehiculos.lista.append(vehiculo)
        Vehiculos.guardar()
        return vehiculo

    @staticmethod
    def borrar(numerodebastidor):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.numerodebastidor == numerodebastidor:
                vehiculo = Vehiculos.lista.pop(indice)
                Vehiculos.guardar()
                return vehiculo

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Vehiculos.lista:
                if type(vehiculo).__name__ == "Coche":
                    writer.writerow((type(vehiculo).__name__, vehiculo.numerodebastidor, vehiculo.color, vehiculo.ruedas, vehiculo.velocidad, vehiculo.cilindrada))
                elif type(vehiculo).__name__ == "Bicicleta":
                    writer.writerow((type(vehiculo).__name__, vehiculo.numerodebastidor, vehiculo.color, vehiculo.ruedas, vehiculo.tipo))
                elif type(vehiculo).__name__ == "Formula1":
                    writer.writerow((type(vehiculo).__name__, vehiculo.numerodebastidor, vehiculo.color, vehiculo.ruedas, vehiculo.velocidad, vehiculo.cilindrada, vehiculo.equipo))
                elif type(vehiculo).__name__ == "Camioneta":
                    writer.writerow((type(vehiculo).__name__, vehiculo.numerodebastidor, vehiculo.color, vehiculo.ruedas, vehiculo.velocidad, vehiculo.cilindrada, vehiculo.carga))
                elif type(vehiculo).__name__ == "Motocicleta":
                    writer.writerow((type(vehiculo).__name__, vehiculo.numerodebastidor, vehiculo.color, vehiculo.ruedas, vehiculo.tipo, vehiculo.velocidad, vehiculo.cilindrada))
                elif type(vehiculo).__name__ == "Quad":
                    writer.writerow((type(vehiculo).__name__, vehiculo.numerodebastidor, vehiculo.color, vehiculo.ruedas, vehiculo.velocidad, vehiculo.cilindrada, vehiculo.tipo, vehiculo.modelo, vehiculo.carga))