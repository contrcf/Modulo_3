import pytest
from src.calculadora.operaciones.MulDiv import division

def obtener_datos_test_division():
    """Regresa los datos necesarios para generar la validacion de la funcion """
    return [("-15/4", "1/2", -7.5), (8, "16", 0.5)]

@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_division())
def test_division_parametrize(num1, num2, esperado):
     """valida la funcion de la operacion de dos valores.
    Parameters
    ----------
    num1 : `int`
        Valor entero utilizado para validacion de  la operacion 
    num2: `int`
        Valor entero utilizado para validacion de  la operacion 
    esperado: `str`
        Valor entero esperado en la operacion 

    Returns
    -------
     result: `bool`
        Determina si la validacion fue exitosa o no 
    """            
     assert division(num1, num2) == esperado




