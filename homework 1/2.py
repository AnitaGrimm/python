n = int(input('n='))

A = [True for i in range(0,n+1)]
if n>=0:
    A[0] = False
if n>=1:
    A[1] = False

#решето эратосфена
i=2;
while i**2<=n:
    if A[i]:
        j=i**2
        while j<=n:
            A[j]=False
            j+=i
    i+=1

print("Все простые числа от 0 до %d:\n"%n,
      ", ".join([str(i) for i in range(n+1) if A[i]]),
      sep="")
