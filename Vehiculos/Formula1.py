import Vechiculo 
import Coche 
class Formula1(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, equipo):   
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.equipo = equipo
    def __str__(self):
        return Coche.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada, self.equipo)