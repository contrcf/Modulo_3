from src.calculadora.utils.utils import obtener_fracciones

def suma(a, b):
    """Operacion de suma de dos valores.

    Parameters
    ----------
    a : `int`
        Valor entero utilizado en la operacion de suma
    b : `int`
        Valor entero utilizado en la operacion de suma

    Returns
    -------
    sumando_a + sumando_b : `int`
        Regresa el resultado de la operacion
    """
    sumando_a = obtener_fracciones(a)
    sumando_b = obtener_fracciones(b)
    return sumando_a + sumando_b

def resta(a, b):
    """Operacion de resta de dos valores.

    Parameters
    ----------
    a : `int`
        Valor entero utilizado en la operacion de resta
    b : `int`
        Valor entero utilizado en la operacion de resta

    Returns
    -------
    minuendo - sustraendo : `int`
        Regresa el resultado de la operacion
    """
   
    minuendo = obtener_fracciones(a)
    sustraendo = obtener_fracciones(b)
    return minuendo - sustraendo