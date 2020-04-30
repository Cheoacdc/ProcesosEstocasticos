from Classes.PMD import PMD
from Classes.Menu import Menu
from utils.Functions import check_int


def init():
    print('Bienvenido al programa para hallar mejor política de un Proceso Markoviano de Decisión.')
    problema = set_problema()
    menu = Menu(problema)
    menu.start()


def set_problema() -> PMD:
    print('Por favor ingrese los datos del PMD: ')
    m = get_param('m')
    k = get_param('k')
    return PMD(m, k)


def get_param(param) -> int:
    while True:
        val = check_int(input(f'¿Cuál es el valor de {param}?: '))
        if val is not None and val > 0:
            break
        else:
            print('Ingrese un número entero mayor a cero...')
    return val


init()
