from typing import List
from MatrizDecision import MatrizDecision
from Functions import check_int


class PMD:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.matrices_decision = {}
        self.politicas = []
        self.set__all_matrices()

    def set__all_matrices(self) -> None:
        for k in range(1, self.k + 1):
            self.matriz_decision_k(k)

    def get_disponible(self, k: int) -> List:
        while True:
            n = input(f'Seleccione el número de estados posibles para la decisión k = {k}: ')
            n = check_int(n)
            if n is not None and n is not 0 and n < self.m + 2:
                break
            else:
                print(f'Ingrese un número entero entre 1 y {self.m + 1}...')
        if n == self.m + 1:
            return [x for x in range(0, self.m + 1)]
        disponible = []
        print('Ahora, ingrese los estados posibles: ')
        while len(disponible) < n:
            e = int(input('Estado disponible: '))
            disponible.append(e)
        return disponible

    def matriz_decision_k(self, k: int) -> None:
        disponible = self.get_disponible(k)
        matriz_k = MatrizDecision(k, disponible)
        matriz_k.set_matriz(self.m)
        self.matrices_decision[k] = matriz_k


