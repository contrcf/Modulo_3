import pytest

from src.calculadora.operaciones.MulDiv import division, multiplica
from src.calculadora.operaciones.SumRes import suma, resta 
from src.calculadora.operaciones.Exponent import exponente

def obtener_datos_test_integracion():
    """ """
    return [("2/2", 2, 3, 4, 16 )]

@pytest.mark.parametrize(
    "num1, num2, num3, num4, esperado", obtener_datos_test_integracion()
)
def test_divide_parametrize(num1, num2, num3, num4, esperado):
    """

    Parameters
    ----------
    num1 : 
        Valor entero utilizado para validacion de  la operacion 
    num2 :
        Valor entero utilizado para validacion de  la operacion      
    num3 :
        Valor entero utilizado para validacion de  la operacion  
    num4 :
        Valor entero utilizado para validacion de  la operacion  
    esperado :
        Valor entero utilizado para validacion de  la operacion
    Returns
    -------
     result: `bool`
        Determina si la validacion fue exitosa o no 
    """ 
    assert(exponente(division(multiplica(suma(num1, num2) + resta(num4,num3), num2),num2),num2)) == esperado
                 