import csv
import config
import helpers
import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Vehiculos.lista = [
            db.Bicicleta("59Y","amarilla","2","urbana"),
            db.Quad("66F","azul","4","63","329","urbana","trail","1000"),
            db.Formula("134X","rojo","4","300","796","ferrari") ]

    def test_buscar_vehiculo(self):
        vehiculo_existente = db.Vehiculos.buscar('11A')
        vehiculo_inexistente = db.Vehiculos.buscar('77G')
        self.assertIsNotNone(vehiculo_existente)
        self.assertIsNone(vehiculo_inexistente)

    def test_crear_vehiculo(self):
        nuevo_vehiculo = db.Vehiculos.crear('2', '22B', 'azul', '2', 'urbana')
        self.assertEqual(len(db.Vehiculos.lista), 4)
        self.assertEqual(nuevo_vehiculo.id, '22B')
        self.assertEqual(nuevo_vehiculo.color, 'azul')
        self.assertEqual(nuevo_vehiculo.ruedas, '2')
        self.assertEqual(nuevo_vehiculo.tipo, 'urbana')

    def test_borrar_vehiculo(self):
        vehiculo_borrado = db.Vehiculos.borrar('11A')
        vehiculo_rebuscado = db.Vehiculos.buscar('11A')
        self.assertEqual(vehiculo_borrado.numerodebastidor, '11A')
        self.assertIsNone(vehiculo_rebuscado)

    def test_numerodebastidor_valido(self):
        self.assertTrue(helpers.numerodebastidor_valido('00A', db.Vehiculos.lista))
        self.assertFalse(helpers.numerodebastidor_valido('232323S', db.Vehiculos.lista))
        self.assertFalse(helpers.numerodebastidor_valido('F35', db.Vehiculos.lista))
        self.assertFalse(helpers.numerodebastidor_valido('11A', db.Vehiculos.lista))

    def test_escritura_csv(self):
        db.Vehiculos.borrar('11A')
        db.Vehiculos.borrar('55E')

        vehiculo, numerodebastidor, color, ruedas, velocidad, cilindrada, tipo, modelo, carga = None, None, None, None, None, None, None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            vehiculo, numerodebastidor, color, ruedas, velocidad, cilindrada, tipo, modelo, carga= next(reader)

        self.assertEqual(vehiculo, 'Quad')
        self.assertEqual(numerodebastidor, '66F')
        self.assertEqual(color, 'negro')
        self.assertEqual(ruedas, '4')
        self.assertEqual(velocidad, '200')
        self.assertEqual(cilindrada, '2000')
        self.assertEqual(tipo, 'urbana')
        self.assertEqual(modelo, 'modelo')
        self.assertEqual(carga, '1000')
