"""
calcule: 
- > derivada de primeira ordem 
-> primitiva (integral sem limites de integração).

obs.:O sympy não acrescenta constantes para integrais indefinidas, 
elas devem ser acrescentadas manualmente.
"""

import sympy as sp

x = sp.symbols('x')
A_x = sp.exp(x)
B_x = x**3
C_x = 1/x

#para adicionar a constante de integraçã
C1 = sp.symbols('C1')

#derivada de A_x
sp.diff(A_x,x)

#integral indefin¡da (sem os limites)
integral_A_x = sp.integrate(A_x,x) 

#acrescentando a constante 
integral_A_x += C1
integral_A_x

#B_x
sp.diff(B_x,x)
sp.integrate(B_x,x)

#C_x
sp.diff(C_x,x)
sp.integrate(C_x,x)

