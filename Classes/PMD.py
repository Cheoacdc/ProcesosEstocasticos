from typing import List, Dict
from Classes.MatrizDecision import MatrizDecision
from Classes.Sistema_de_ecuaciones import SistemaDeEcuaciones
from utils.Functions import check_int, confirmacion, check_index


class PMD:
    def __init__(self, m: int, k: int, matrices_decision: Dict = None, tipo: str = 'min'):
        self.m = m
        self.k = k
        self.politicas = []
        self.costos = {}
        self.tipo = tipo
        if matrices_decision:
            self.matrices_decision = matrices_decision
        else:
            self.matrices_decision = {}
            self.set_all_matrices()

    def set_all_matrices(self) -> None:
        for k in range(1, self.k + 1):
            self.matriz_decision_k(k)

    def get_disponible(self, k: int) -> List:
        while True:
            n = input(f'Seleccione el número de estados posibles para la decisión k = {k}: ')
            n = check_int(n)
            if n is None or not 0 < n < self.m + 2:
                print(f'Ingrese un número entero entre 1 y {self.m + 1}...')
            elif confirmacion('¿Los datos ingresados son correctos?'):
                break
        while True:
            if n == self.m + 1:
                return [x for x in range(0, self.m + 1)]
            disponible = []
            print('Ahora, ingrese los estados posibles: ')
            while len(disponible) < n:
                e = int(input('Estado disponible: '))
                disponible.append(e)
            if confirmacion('¿Los datos ingresados son correctos?'):
                break
        disponible.sort()
        return disponible

    def matriz_decision_k(self, k: int) -> None:
        disponible = self.get_disponible(k)
        matriz_k = MatrizDecision(k, disponible, tipo=self.tipo)
        matriz_k.set_matriz(self.m)
        self.matrices_decision[k] = matriz_k

    def posibles_k_para_e(self, e: int) -> List:
        ks = []
        for k in range(1, self.k + 1):
            if check_index(e, self.matrices_decision[k].estados) is not None:
                ks.append(k)
        return ks

    def get_costos(self):
        for i in self.matrices_decision:
            for costo in self.matrices_decision[i].costos:
                self.costos[costo] = self.matrices_decision[i].costos[costo]

    def get_matriz_de_politica(self, politica: List) -> Dict:
        resultado = self.evaluar_politica(politica)
        matriz = resultado['matriz']
        costo = resultado['costo']
        return {'matriz': matriz, 'costo_esperado': costo, 'politica': politica}

    def evaluar_politica(self, politica: List) -> Dict:
        matriz = []
        costos = []
        for e, k in enumerate(politica):
            mat_k = self.matrices_decision[k]
            index = mat_k.estados.index(e)
            row = [val for val in mat_k.matriz[index]]
            matriz.append(row)
            costo = mat_k.costos[f'c{e}{k}']
            costos.append(costo)
        costo_esperado = self.costo_esperado(matriz, costos)
        return {'matriz': matriz, 'costo': costo_esperado}

    def costo_esperado(self, matriz: List, costos: List):
        sistema_ecuaciones = SistemaDeEcuaciones(matriz, costos, self.m, metodo='exhaustivo')
        sistema_ecuaciones.resolver_sistema()
        return sistema_ecuaciones.solucion
