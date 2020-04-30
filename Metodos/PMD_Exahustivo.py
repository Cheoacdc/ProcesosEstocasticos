from Classes.PMD import PMD
from typing import List, Dict
from utils.Functions import confirmacion


class PMDExahustivo(PMD):
    def __init__(self, m: int, k: int, matrices_decision: Dict = None):
        super().__init__(m, k, matrices_decision)
        self.matrices_de_politica = {}

    def generar_politicas(self) -> None:
        self.get_politica([])

    def get_politica(self, nums: List) -> None:
        if len(nums) < self.m + 1:
            e = len(nums)
            for d in range(1, self.k + 1):
                if e not in self.matrices_decision[d].estados:
                    continue
                else:
                    aux_nums = [num for num in nums]
                    aux_nums.append(d)
                    self.get_politica(aux_nums)
        else:
            self.politicas.append(nums)

    def fill_matrices_de_politica(self):
        for i, politica in enumerate(self.politicas):
            self.set_matriz_de_politica(politica, i)

    def set_matriz_de_politica(self, politica: List, num: int):
        resultado = self.evaluar_politica(politica)
        matriz = resultado['matriz']
        costo = resultado['costo']
        self.matrices_de_politica[f'R{num}'] = {'matriz': matriz, 'costo_esperado': costo, 'politica': politica}

    def get_mejor_politica(self) -> Dict:
        mejor = {'costo': ''}
        for i, nombre in enumerate(self.matrices_de_politica):
            if mejor['costo'] == "" or mejor['costo'] > self.matrices_de_politica[nombre]['costo_esperado']:
                mejor['costo'] = self.matrices_de_politica[nombre]['costo_esperado']
                mejor['politica'] = self.matrices_de_politica[nombre]['politica']
                mejor['nombre'] = nombre
        return mejor

    def mostrar_politicas(self):
        print('Se generaron las siguientes posibles políticas:')
        for politica in self.matrices_de_politica:
            print(f'\tPolitica: {self.matrices_de_politica[politica]["politica"]}')
            print('\tMatriz: ')
            for row in self.matrices_de_politica[politica]["matriz"]:
                print(f'\t\t{row}')
            print(f'\tCosto esperado: {self.matrices_de_politica[politica]["costo_esperado"]}\n')

    def resolver(self) -> Dict:
        self.generar_politicas()
        self.fill_matrices_de_politica()
        if confirmacion('¿Desea mostrar cada política generada?'):
            self.mostrar_politicas()
        return self.get_mejor_politica()
