def obtener_fracciones(frac_str):
    """Convierte un valor en fraccion a decimal.

    Parameters
    ----------
    frac_str : `str`
        obtiene la fraccion en string
        
    Returns
    -------
    frac_str : `float`
        Regresa el valor de la fraccion convertido a flotante
    """
    if isinstance(frac_str, (int, float)):
        return frac_str
    if "/" in frac_str:
        try:
            return float(frac_str)
        except ValueError:
            num, denom = frac_str.split("/")
            try:
                leading, num = num.split(" ")
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac
    return float(frac_str)
