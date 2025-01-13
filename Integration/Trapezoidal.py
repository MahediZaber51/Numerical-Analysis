def trapezoidal(x,y,n):
    h = x[1]-x[0]
    s = 0
    for i in range(1,n-1):
        s += y[i]
    return h*(y[0]+y[n-1]+2*s)/2
    
    

x = []
y = []
n = int(input("Enter the number of data: "))
if n < 1:
    print("At least two data required.")
    exit()
for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))
print(trapezoidal(x,y,n))
