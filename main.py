from Interpolation.Lagrange import lagrange

from Integration.Simpson.one_third import one_third
from Integration.Simpson.three_eighth import three_eighth
from Integration.Trapezoidal import trapezoidal
from Integration.Weddle import weddle

from ODE.Euler import euler
from ODE.Euler.Modified import euler_modified
from ODE.Runge_Kutta.Fourth_Order import fourth_order
from ODE.Runge_Kutta.Second_Order import second_order



x = []
y = []
n = int(input("Enter the number of data: "))
if n < 1:
    print("At least two data required.")
    exit()
for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))
    
    
# Under Construction :)
# Under Construction :)
# Under Construction :)