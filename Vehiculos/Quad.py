import Vehiculos 
import Bicicleta
import Coche
class Quad(Coche, Bicicleta):
    def __init__(self, color, ruedas, velocidad, cilindrada, tipo, modelo):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.modelo = modelo

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc, {}, {}".format(self.velocidad, self.cilindrada, self.tipo, self.modelo)
