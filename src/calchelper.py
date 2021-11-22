# import scipy.integrate as integrate
# import scipy.special as special
from sympy import *
init_printing(use_unicode=False, wrap_line=False)


def h_integrate(equation, by, nonsimplify):
    """ 
    Parameters:
    -------
    - equation: the actual equation
    - by: eg. dx or (dx, from, to)
    - nonsimplify: bool for simplification
    """

    print('\n')
    print('Input: \n')
    print(pretty(nsimplify(Integral(equation, by))))
    print('\n')
    print('Result: \n')
    result = 0
    if (nonsimplify):
        result = integrate(equation, by)
    else:
        result = nsimplify(integrate(equation, by))
    print(pretty(result))
    return result


def h_diff(equation, by, nonsimplify):
    """ 
    Parameters:
    -------
    - equation: the actual equation
    - by: eg. dx
    - nonsimplify: bool for simplification
    """

    print('\n')
    print('Input: \n')
    print(pretty(nsimplify(Derivative(equation, by))))
    print('\n')
    print('Result: \n')
    result = 0
    if (nonsimplify):
        result = diff(equation, by)
    else:
        result = nsimplify(diff(equation, by))
    print(pretty(result))
    return result
