from src.calculadora.utils.utils import obtener_fracciones

def multiplica(a, b):
    """Operacion de multiplicacion con dos valores.
    Parameters
    ----------
    a : `int`
        Valor entero utilizado en la operacion de multiplicacion
    b : `int`
        Valor entero utilizado en la operacion de multiplicacion

    Returns
    -------
    multiplicando * multiplicador : `int`
        Regresa el resultado de la operacion
    """
    multiplicando = obtener_fracciones(a)
    multiplicador = obtener_fracciones(b)
    return multiplicando * multiplicador

def division(a, b):
    """Operacion de division con dos valores.
    Parameters
    ----------
    a : `int`
        Valor entero utilizado en la operacion de multiplicacion
    b : `int`
        Valor entero utilizado en la operacion de multiplicacion

    Returns
    -------
    multiplicando * multiplicador : `int`
        Regresa el resultado de la operacion
    """
    dividendo = obtener_fracciones(a)
    divisor = obtener_fracciones(b)
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "Division entre cero"