from PMD import PMD
from Metodos.PMD_Exahustivo import PMDExahustivo
from Metodos.Prog_Lineal import ProgLineal
from Metodos.Mejoramiento_Politicas import MejoramientoPoliticas
from utils.Functions import check_int, confirmacion
from typing import Dict


class Menu:
    def __init__(self, problema: PMD):
        self.problema = problema
        self.metodos = {
            '1': PMDExahustivo,
            '2': ProgLineal,
            '3': MejoramientoPoliticas
        }

    @classmethod
    def get_opcion(cls) -> str:
        print('Seleccione el método que desea emplear para resolver el problema:')
        print('\t1) Enumeración exahustiva de políticas')
        print('\t2) Solución por programación lineal')
        print('\t3) Método de mejoramiento de políticas')
        print('\t4) Método de mejoramiento de políticas con descuento')
        print('\t5) Método de aproximaciones sucesivas')
        while True:
            opc = check_int(input('Ingrese el número del método que desea emplear: '))
            if opc is None or opc > 5 or opc < 1:
                print('Por favor ingrese un número entre 1 y 5')
            else:
                break
        return str(opc)

    @classmethod
    def mostrar_solucion(cls, solucion: Dict):
        print(f'Se determinó que la mejor política fue: {solucion["politica"]}')
        print(f'El costo esperado al aplicar dicha politica es: {solucion["costo"]}')

    def start(self):
        while True:
            opcion = self.get_opcion()
            metodo = self.metodos[opcion](self.problema.m, self.problema.k, self.problema.matrices_decision)
            solucion = metodo.resolver()
            self.mostrar_solucion(solucion)
            if not confirmacion('¿Desea resolver por otro método?'):
                break
        print('Saliendo del programa...')
