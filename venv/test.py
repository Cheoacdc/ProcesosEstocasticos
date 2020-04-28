import numpy as np
from typing import List
from utils.PPL import PPL
from scipy.optimize import minimize, linprog

def objective(x, costos):
    obj = 0
    for i, x in enumerate(x):
        obj += x*costos[i]
    return obj

def constraint_maker(coeficients):
    def constraint(x):
        return np.dot(x, coeficients)
    return constraint

def generate_constraints(coeficients_mat: List):
    cons = []
    for row in coeficients_mat:
        fun = constraint_maker(row)
        constraint = {'type': 'eq', 'fun': fun}
        cons.append(constraint)
    return cons

coeficientes = [
    [1,1,1,1,1,1],
    [1, -1, 0, 0, -1, -1],
    [-.825, 1/4, 1, 0, 0, 0]
]
x0 = np.zeros(6)
costos = [10,20,10,5, 5, 10]
b = (0, np.inf)
bounds = [b,b,b,b,b,b]

cons = generate_constraints(coeficientes)
sol = minimize(objective, x0, args=(costos), method='SLSQP', bounds=bounds, constraints=cons)
print(sol)

'''
def set_matriz_de_politica(self, politica: List, matrices_de_politica: Dict = None, num: int = 0):
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
    if matrices_de_politica is not None:
        matrices_de_politica[f'R{num}'] = {'matriz': matriz, 'costo_esperado': costo_esperado, 'politica': politica}
    else:
        return {'costo': costo_esperado, 'politica': politica}


def costo_esperado(self, matriz: List, costos: List):
    sistema_ecuaciones = SistemaDeEcuaciones(matriz, costos, self.m)
    sistema_ecuaciones.resolver_sistema()
    return sistema_ecuaciones.solucion '''
