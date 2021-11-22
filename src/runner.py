from scipy import stats
from sympy import *
from statshelper import *
from calchelper import *

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

# Notes:
# - need all those distribution functions to solve algebra
# - alpha = 1 - CI percentage

# Symbols:
# - oo

# Others:
# - nsimplify(ex, tolerance=0.001, rational=True): to nsimplify 
# - simplify(ex): to simplify

# Calculus (can nest, don't use k for algebra):
# - h_integrate
# - h_diff

# Stats
# - convertPZfromAlpha2
# - convertPZfromAlphaN
# - convertPZ
# - convertT


#examples
#h_integrate((1-exp(-8*x)), (x, 0, 12/60))
#pprint(solve(integrate(integrate(z * (x**2 + y**2), (x, 3, 5)), (y, 3, 5)) - 1, z))
#print(nsimplify(integrate((2/3)*(x+2*y), (x, 0, 1))))
#convertT(0.050, 7)



calc = convertT(0.050, 7)

pprint(calc)