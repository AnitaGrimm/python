import math

def triangle_square(a,b,c):
    if a==0 or b==0 or c==0:
        return 0
    p=(a+b+c)/2
    Ssq= p*(p-a)*(p-b)*(p-c)
    if Ssq>=0:
        return math.sqrt(Ssq)
    else:
        return float("NaN")

print("Введите стороны треугольника:")
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a>=0 and b>=0 and c>=0:
    print("площадь треугольника S = %.4f"% triangle_square(a,b,c))
else:
     print("данные введены некорректно!")
