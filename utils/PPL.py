from typing import List
import numpy as np
from scipy.optimize import minimize


class PPL:
    def __init__(self, costos: List, coeficientes: List):
        self.costos = costos
        self.coeficientes = coeficientes
        self.n = len(costos)
        self.constraints = []
        self.bounds = [(0, np.inf) for x in range(0, self.n)]
        self.x0 = np.zeros(self.n)

    @classmethod
    def objective(cls, x, costos):
        obj = 0
        for i, x in enumerate(x):
            obj += x * costos[i]
        return obj

    @classmethod
    def constraint_maker(cls, coeficientes: List) -> callable:
        def constraint(x):
            return np.dot(x, coeficientes)

        return constraint

    @classmethod
    def last_constraint_maker(cls, coeficientes: List) -> callable:
        def constraint(x):
            return np.dot(x, coeficientes) - 1

        return constraint

    def generate_constraints(self):
        for i, row in enumerate(self.coeficientes):
            if not i == len(self.coeficientes) - 1:
                fun = self.constraint_maker(row)
            else:
                fun = self.last_constraint_maker(row)
            constraint = {'type': 'eq', 'fun': fun}
            self.constraints.append(constraint)

    def solve(self):
        self.generate_constraints()
        sol = minimize(self.objective, self.x0, args=self.costos,
                       method='SLSQP', bounds=self.bounds, constraints=self.constraints)
        return sol


