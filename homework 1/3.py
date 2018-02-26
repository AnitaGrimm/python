a = int(input("a = "))
b = int(input("b = "))

print("Числа, кратные 5 в промежутке [%d,%d]:\n"%(a,b),
      ", ".join([str(i) for i in range(a,b+1) if i%5==0]),
      sep="")
