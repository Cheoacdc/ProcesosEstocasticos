from typing import List
import os
import sys


def check_int(num: str) -> int or None:
    try:
        result = int(num)
    except ValueError:
        return None
    return result


def check_float(flt: str) -> float or None:
    if '/' in flt:
        helper = []
        nums = flt.split('/')
        if len(nums) is not 2:
            return None
        for val in nums:
            helper.append(check_int(val))
        if all(helper):
            number = int(helper[0]) / int(helper[1])
        else:
            return None
    else:
        try:
            number = float(flt)
        except ValueError:
            return None
    return number


def check_index(element: str or int or float, lista: List) -> int or None:
    try:
        result = lista.index(element)
    except ValueError:
        return None
    return result


def get_alpha() -> float:
    while True:
        alpha = check_float(input('Ingrese el valor de alpha(descuento): '))
        if alpha is not None and 0 < alpha < 1:
            break
        print('Ingrese un valor en el siguiente intervalo: (0, 1)')
    return alpha


def get_param(param, fun: str = 'int') -> int:
    while True:
        val = func_switcher[fun](input(f'¿Cuál es el valor de {param}?: '))
        if val is not None and val > 0:
            break
        else:
            print('Ingrese un número entero mayor a cero...')
    return val


def confirmacion(msg: str = '¿Desea continuar?') -> bool:
    while True:
        respuesta = input(f'{msg} (Si/No): ')
        if respuesta.lower() == 'si' or respuesta == '':
            return True
        elif respuesta.lower() == 'no':
            return False
        else:
            print('Ingrese una opción aceptada...')
            continue


def clear_screen():
    if sys.platform[:3] == 'win':
        os.system('cls')
    if sys.platform[:5] == 'linux' or sys.platform[:6] == 'darwin':
        os.system('clear')


func_switcher = {
    'int': check_int,
    'float': check_float
}
