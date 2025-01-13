def euler_modified(f, x0, y0, h, target):
    x = x0
    y = y0
    while x < target:
        y_euler = y + h * f(x, y) 
        y = recursive_y(f, x, y, y_euler, h) 
        x = x + h
    return [x, y]

def recursive_y(f, x, y, y1, h, steps=3):
    for i in range(steps):
        y1 = y + (h / 2) * (f(x, y) + f(x + h, y1))
    return y1

def f(x, y):
    return (x * y) + 1 # Change this function to match the function you want to solve


x0 = float(input("Enter the initial value of x (x0): "))
y0 = float(input("Enter the initial value of y (y0): "))
h = float(input("Enter the step size (h): "))
target = float(input("Enter the target value of x: "))
print(euler_modified(f, x0, y0, h, target))
