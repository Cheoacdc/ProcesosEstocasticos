from Classes.PMD import PMD
from Classes.Menu import Menu
from utils.Functions import get_param, clear_screen


def init():
    clear_screen()
    print('Bienvenido al programa para hallar mejor política de un Proceso Markoviano de Decisión.')
    problema = set_problema()
    menu = Menu(problema)
    menu.start()


def set_problema() -> PMD:
    print('Por favor ingrese los datos del PMD: ')
    m = get_param('m')
    k = get_param('k')
    return PMD(m, k)


init()
