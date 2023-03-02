import unittest
from Vehiculos.Camioneta import Camioneta
class TestCamioneta(unittest.TestCase):
    def test_camioneta(self):
        camioneta = Camioneta("rojo", 4, 120, 1000, 2000)
        self.assertEqual(camioneta.color, "rojo")
        self.assertEqual(camioneta.ruedas, 4)
        self.assertEqual(camioneta.velocidad, 120)
        self.assertEqual(camioneta.cilindrada, 1000)
        self.assertEqual(camioneta.carga, 2000)
        self.assertEqual(str(camioneta), "rojo, 4 ruedas, 120 km/h, 1000cc, 2000 kg")