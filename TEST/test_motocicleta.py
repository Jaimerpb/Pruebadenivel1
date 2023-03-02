import unittest 
from Vehiculos.Motocicleta import Motocicleta
class TestMotocicleta(unittest.TestCase):
    def test_motocicleta(self):
        motocicleta = Motocicleta("rojo", 2, 120, 1000)
        self.assertEqual(motocicleta.color, "rojo")
        self.assertEqual(motocicleta.ruedas, 2)
        self.assertEqual(motocicleta.velocidad, 120)
        self.assertEqual(motocicleta.cilindrada, 1000)
        self.assertEqual(str(motocicleta), "rojo, 2 ruedas, 120 km/h, 1000cc")
