def fourth_order(f,x0,x1,y1,h):
    k1 = h*f(x0+h,y1)
    k2 = h*f(x1+h/2,y1+k1/2)
    k3 = h*f(x1+h/2,y1+k2/2)
    k4 = h*f(x1+h,y1+k3)
    y = y1 + (k1+2*k2+2*k3+k4)/6
    x = x1 + h
    return x,y

def f(x,y):
    return x*x + y  # Change this function to match the function you want to solve

x0 = float(input("Enter the initial value of x (x0): "))
x1 = float(input("Enter the next value of x (x1): "))
y1 = float(input("Enter the initial value of y (y1): "))
h = float(input("Enter the step size (h): "))
print(fourth_order(f,x0,x1,y1,h))