def one_third(x,y,n):
    if (n - 1) % 2 != 0:
        print("Simpson's 1/3 rule can only be applied with an even number of stripes.")
        exit()
    h = x[1]-x[0]
    s = 0
    for i in range(1,n- 1):
        if i%2 == 0:
            s += 2*y[i]
        else:
            s += 4*y[i]
    return h*(y[0]+y[n- 1]+s)/3



x = []
y = []
n = int(input("Enter the number of data: "))
if n < 2:
    print("At least three data required.")
    exit()
for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))
    
print(one_third(x, y, n))