import pytest
from src.calculadora.operaciones.Exponent import exponente

def obtener_datos_test_exponente():
    """Regresa los datos necesarios para generar la validacion de la funcion """
    return [(5,2, 25), (8,2,64)]

@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_exponente())
def test_exponent_parametrize(num1, num2, esperado):
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
   assert exponente(num1, num2) == esperado
