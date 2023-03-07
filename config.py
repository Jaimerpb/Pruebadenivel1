import sys

DATABASE_PATH = "Vehiculos.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "test/vehiculos_test.csv"
