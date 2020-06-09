from Classes.PMD import PMD
from Metodos.PMD_Exahustivo import PMDExahustivo
from Metodos.Prog_Lineal import ProgLineal
from Metodos.Mejoramiento_Politicas_Descuento import MejoramientoPoliticas, MejoramientoPoliticasDescuento
from Metodos.Aproximaciones_Sucesivas import AproximacionesSucesivas
from utils.Functions import check_int, confirmacion, clear_screen
from typing import Dict


class Menu:
    def __init__(self, problema: PMD):
        self.problema = problema
        self.metodos = {
            '1': PMDExahustivo,
            '2': ProgLineal,
            '3': MejoramientoPoliticas,
            '4': MejoramientoPoliticasDescuento,
            '5': AproximacionesSucesivas
        }

    @classmethod
    def get_opcion(cls) -> str:
        clear_screen()
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

    def mostrar_solucion(self, solucion: Dict):
        print(f'-> Se determinó que la mejor política fue: {solucion["politica"]}')
        costo = solucion["costo"] if self.problema.tipo == 'min' else -1 * solucion['costo']
        print(f'-> El costo esperado al aplicar dicha politica es: {costo}')

    def start(self):
        while True:
            opcion = self.get_opcion()
            metodo = self.metodos[opcion](self.problema.m, self.problema.k,
                                          self.problema.matrices_decision, tipo=self.problema.tipo)
            solucion = metodo.resolver()
            self.mostrar_solucion(solucion)
            if not confirmacion('¿Desea resolver por otro método?'):
                break
        print('Saliendo del programa...')
