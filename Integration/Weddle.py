def weddle(x,y,n):
    if (n - 1) % 6 != 0:
        print("Weddle's rule can only be applied with a number of stripes that is a multiple of 6.")
        exit()
    h = x[1]-x[0]
    s = 0
    for i in range(0, n-1, 6):
        s += 1 * y[i]
        s += 5 * y[i+1]
        s += 1 * y[i+2]
        s += 6 * y[i+3]
        s += 1 * y[i+4]
        s += 5 * y[i+5]
        s += 1 * y[i+6]
    return 3*h*s/10

x = []
y = []
n = int(input("Enter the number of data points: "))
if n < 6:
    print("At least seven data points are required.")
    exit()
for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))

print(weddle(x, y, n))