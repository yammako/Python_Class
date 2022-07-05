print(0.1 + 0.05)
from decimal import Decimal
from http.client import NETWORK_AUTHENTICATION_REQUIRED
x = Decimal('0.1') + Decimal('0.05')
print(x)

print(Decimal(0.1))

from fractions import Fraction
print(Fraction(0.1))

import numpy as np
x0 = 1
x1 = 2
tol = 1e-15

def f(x):
    return np.sqrt(x+1)*np.cos(x/2)**3

for i in range(500):
    fx0 = f(x0)
    fx1 = f(x1)

    x2 = x1 - fx1 * (x1 - x0)/(fx1 - fx0)

    interval = abs(x2 - x1)/abs(x1)

    if interval <= tol:
        N = i + 1
        rootFound = True
        break
    else:
        rootFound = False

    x0 = x1
    x1 = x2

if rootFound:
    print('After {} iterations, the root is {}'.format(N, x2))
else:
    print('Secant method did not converge.')

import numpy as np
from scipy.optimize import newton
f = lambda x: x**3 - 7*x - 19
df = lambda x: 3*x**2 - 7
x0 = 5
c = newton(f, x0, df)
print(c)