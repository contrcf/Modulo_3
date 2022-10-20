import pytest

from src.calculadora.operaciones.MulDiv import multiplica

def obtener_datos_test_multiplica():
    """Regresa los datos necesarios para generar la validacion de la funcion """
    return [(-1, 1, -1), (10, "5", 50)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_multiplica())
def test_multiplica_parametrize(num1, num2, esperado):
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
     assert multiplica(num1, num2) == esperado


