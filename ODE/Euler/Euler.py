def euler(f, x0, y0, h, target):
    x = x0
    y = y0
    while True:
        y = y + h * f(x, y)
        x = x + h
        if x >= target:
            break
    return [x,y]

def f(x, y):
    return (x*y)+1  # Change this function to match the function you want to solve

x0 = float(input("Enter initial value of x (x0): "))
y0 = float(input("Enter initial value of y (y0): "))
h = float(input("Enter step size (h): "))
x = float(input("Enter target x value: "))
print(euler(f, x0, y0, h,x))
