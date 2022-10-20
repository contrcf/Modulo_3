
import pytest

from src.calculadora.operaciones.SumRes import resta

def obtener_datos_test_resta():
    """Regresa los datos necesarios para generar la validacion de la funcion """
    return [(0.5, 0.5, 0), ("2/2", "1", 0)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_resta())
def test_resta_parametrize(num1, num2, esperado):
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
     assert resta(num1, num2) == esperado
