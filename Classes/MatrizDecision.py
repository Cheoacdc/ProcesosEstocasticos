from typing import List
from utils.Functions import check_float, confirmacion


class MatrizDecision:
    def __init__(self, k: int, estados: List):
        self.k = k
        self.estados = estados
        self.matriz = []
        self.costos = {}

    def get_costo(self, i: int) -> float:
        while True:
            costo = input(f'Ingrese el costo C{i}{self.k}: ')
            costo = check_float(costo)
            if costo is None:
                print('Valor inválido, intente de nuevo...')
                continue
            else:
                break
        return costo

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
                suma = sum(row)
                if not .999999 < suma < 1.000001:
                    print('La suma de probabilidades debe ser igual a 1')
                    continue
                costo = self.get_costo(i)
                print(f'Los valores ingresados para el estado {i} son: {row}')
                print(f'El costo ingresado es: {costo}')
                if confirmacion():
                    break
            self.matriz.append(row)
            self.costos[f'c{i}{self.k}'] = costo
