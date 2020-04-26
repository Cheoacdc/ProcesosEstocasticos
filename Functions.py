def check_int(num: str):
    try:
        result = int(num)
    except ValueError:
        return None
    return result


def check_float(flt: str):
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


def confirmacion():
    while True:
        respuesta = input('¿Desea continuar? (Si/No): ')
        if respuesta.lower() == 'si' or respuesta == '':
            return True
        elif respuesta.lower() == 'no':
            return False
        else:
            print('Ingrese una opción aceptada...')
            continue
