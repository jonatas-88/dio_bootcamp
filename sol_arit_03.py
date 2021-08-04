
#a = [float(x) for x in input().split()]

a = [6,4,2.1]

if a[0] + a[1] > a[2] and a[1] + a[2] > a[0] and a[1] + a[2] > a[2]:  
    print(f"Perimetro = {sum(a):.1f}")
else:
    print(f"Area = {((a[0] + a[1]) * a[2]) / 2:.1f}")