def lagrange(x,y,n,z):
    s = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p *= (z-x[j])/(x[i]-x[j])
        s += y[i]*p
    return s
    
    

x = []
y = []
n = int(input("Enter the number of data: "))
if n < 1:
    print("At least two data required.")
    exit()
for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))
z = int(input("Enter the value of x to find the value of y: "))
print(lagrange(x,y,n,z))