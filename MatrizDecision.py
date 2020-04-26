from typing import List
from Functions import check_float, confirmacion
import numpy as np


class MatrizDecision:
    def __init__(self, k: int, estados: List):
        self.k = k
        self.estados = estados
        self.matriz = []
        self.costos = {}

    def set_matriz(self, m: int) -> None:
        for i in self.estados:
            while True:
                row = []
                for j in range(0, m + 1):
                    while True:
                        number = (input(f'Ingrese p{i}{j} en k = {self.k}: '))
                        prob = check_float(number)
                        if prob is not None:
                            row.append(prob)
                            break
                        else:
                            print('Valor inválido, intente de nuevo...')
                costo = input(f'Ingrese el costo C{i}{self.k}: ')
                print(f'Los valores ingresados para el estado {i} son: {row}')
                print(f'El costo ingresado es: {costo}')
                if confirmacion():
                    break
            self.matriz.append(row)
            self.costos[f'c{i}{self.k}'] = costo
