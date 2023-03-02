import unittest
from Vehiculos.Bicicleta import Bicicleta 
class TestBicicleta(unittest.TestCase):
    def test_bicicleta(self):
        bicicleta = Bicicleta("rojo", 2, "urbana")
        self.assertEqual(bicicleta.color, "rojo")
        self.assertEqual(bicicleta.ruedas, 2)
        self.assertEqual(bicicleta.tipo, "urbana")
        self.assertEqual(str(bicicleta), "rojo, 2 ruedas, urbana")

