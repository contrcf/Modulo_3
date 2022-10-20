
import pytest

from src.calculadora.utils.utils import obtener_fracciones

def obtener_datos_test_obtener_fracciones():
    """Regresa los datos necesarios para generar la validacion de la funcion """
    return [("7/4", 1.75), (10, 10)]


@pytest.mark.parametrize("num1, esperado", obtener_datos_test_obtener_fracciones())
def test_obtener_fracciones_parametrize(num1, esperado):
   """valida la funcion conversion de fraccion de dos valores.
    
    Parameters
    ----------
    num1 : `int`
        Valor entero utilizado en la operacion 
    esperado: `float`
        Valor entero esperado la operacion de multiplicacion

    Returns
    -------
     result: `bool`
        Determina si la validacion fue exitosa o no 
    """     
   assert obtener_fracciones(num1) == esperado

