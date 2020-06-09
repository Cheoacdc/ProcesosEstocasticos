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
    while True:
        tipo = input('¿Se trata de un problema de minimización o maximización? (min/max): ')
        if not (tipo.lower() == 'min' or tipo.lower() == 'max'):
            print('Ingrese una opción válida...')
            continue
        break
    print('Por favor ingrese los datos del PMD: ')
    m = get_param('m')
    k = get_param('k')
    return PMD(m, k, tipo=tipo)


init()
