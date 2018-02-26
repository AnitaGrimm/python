import math, cmath

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a==0:
    print("a=0 => уравнение не является квадратным...\nРешение линейного уравнения:")
    if b==0:
        print("решений нет")
    else:
        if c==0:
            print("x=0")
        else:
            x=-c/b
            print("x=%.2f"%x)
else:
    D=b*b-4*a*c
    print("Решения квадратного уравнения:")
    if D>0:
        x1 = (-b-math.sqrt(D))/2/a; x2 = (-b+math.sqrt(D))/2/a
        print("x1=%.2f, x2=%.2f"%(x1,x2))
    elif D==0:
        x = -b/2/a
        print("x1=x2=%.2f"%x)
    else:
        #решение - комплексное число
        x1 = (-b-cmath.sqrt(D))/2/a; x2 = (-b+cmath.sqrt(D))/2/a
        print("x1=",x1,", x2=",x2,sep="")
    
