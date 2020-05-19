def multiples(n):
    for i in range(1,21,2):
        k = n*i
   
        p = "{}*{} ={}".format(n,i,k)
        print(p)


n=int(input("Enter a number: "))
multiples(n)