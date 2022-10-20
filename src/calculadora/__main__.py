
import sys

from pathlib import Path

from src.calculadora import settings
from src.calculadora.config import ROOT_DIR

from src.calculadora.operaciones.SumRes import suma, resta 
from src.calculadora.operaciones.MulDiv import multiplica, division
from src.calculadora.operaciones.Exponent import exponente

def main(operacion, num_1, num_2):
    """Realiza una operacion matematica dada de dos variables 
    Parameters
    ----------
    operacion :`str`
        Tipo de operacion a realizar
    num_1 :`int`
        Valor entero utilizado para validacion de  la operacion 
    num_2 :`int`
        Valor entero utilizado para validacion de  la operacion 

    Returns
    -------
     Result:`float` 
        Resultado de la operacion dada
    """
    if operacion =="suma" :
         res_suma = suma(num_1, num_2)
         print(settings.TOTAL_SUM,res_suma)
    elif operacion =="resta" :
         res_resta = resta(num_1, num_2)
         print(settings.TOTAL_RES,res_resta) 
    elif operacion =="division" :
         res_divide = division(num_1, num_2)
         print(settings.TOTAL_DIV, res_divide)
    elif operacion =="multiplica" :
         res_multiplica = multiplica(num_1, num_2)
         print(settings.TOTAL_MUL,res_multiplica)
    elif operacion =="exponente" :
         res_exponent = exponente(num_1, num_2)
         print(settings.TOTAL_EXP,res_exponent)
    else:
         print("Operacion Invalida")
             

if __name__ == "__main__":
    
    with open(Path(ROOT_DIR, settings.DATA_PATH, "InitMsg.txt")) as f:
        lines = f.readlines()
    print(lines)

    if len(sys.argv) < 4 :
       print("Parametros Invalidos") 
    else:    
        arg_operacion=sys.argv[1]
        arg_num_1=sys.argv[2]
        arg_num_2=sys.argv[3]
        main(arg_operacion, arg_num_1,arg_num_2)

   