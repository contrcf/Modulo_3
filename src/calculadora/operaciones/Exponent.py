from src.calculadora.utils.utils import obtener_fracciones

def exponente(a, b):
    """Operacion de exponencial con dos valores.

    Parameters
    ----------
    a : `int`
        Valor entero utilizado en la operacion de multiplicacion
    b : `int`
        Valor entero utilizado en la operacion de multiplicacion
        

    Returns
    -------
    valor_base ** valor_exponente : `float`
        Regresa el resultado de la operacion
    """
    valor_base = obtener_fracciones(a)
    valor_exponente = obtener_fracciones(b)
    return valor_base ** valor_exponente
 