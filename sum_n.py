def summation(n):
    a=0
    while (n!=0):
        a=a+n
        n=n-1
    print(a)

n=int(input("enter n: "))
summation(n)