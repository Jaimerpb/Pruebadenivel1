import os
import platform
import re

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto 

def leer_numero(min=0, max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        try:
            numero = input("> ")
            if int(numero) >= min and int(numero) <= max:
                return numero
        except ValueError:
            pass

def catalogar(lista, ruedas=None):
    contador = 0
    for vehiculo in lista:
        if vehiculo.ruedas == ruedas:
            print("{}: {}".format(type(vehiculo).__name__, vehiculo))
            contador +=1
        elif ruedas == None:
            print("{}: {}".format(type(vehiculo).__name__, vehiculo))
    if ruedas != None:
        print("\nSe han encontrado {} vehículos con {} ruedas".format(contador, ruedas))
    return contador

def numerodebastidor_valido(numerodebastidor, lista):
    if not re.match('[0-9]{2}[A-Z]$', numerodebastidor):
        print("numerodebastidor incorrecto, debe cumplir el formato.")
        return False
    for vehiculo in lista:
        if vehiculo.numerodebastidor == numerodebastidor:
            print("numerodebastidor utilizado por otro vehículo.")
            return False
    return True