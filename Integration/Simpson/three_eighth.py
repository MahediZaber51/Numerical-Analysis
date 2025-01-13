def three_eighth(x,y,n):
    if (n - 1) % 3 != 0:
        print("Simpson's 3/8 rule can only be applied with a number of stripes that is a multiple of 3.")
        exit()
    h = x[1]-x[0]
    s = 0
    for i in range(1,n- 1):
        if i%3 == 0:
            s += 2*y[i]
        else:
            s += 3*y[i]
    return 3*h*(y[0]+y[n- 1]+s)/8



x = []
y = []
n = int(input("Enter the number of data: "))
if n < 3:
    print("At least four data required.")
    exit()
for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))
    
print(three_eighth(x, y, n))