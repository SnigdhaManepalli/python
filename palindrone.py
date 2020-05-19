def palin(n):
    rem=0
    temp=0
    tem=n

    while (n!=0):
        rem=n%10
        temp=temp*10+rem
        n=n//10
    print(temp)
    if(temp==tem):
        print("n is a palindrone")
    else:
            print("not a aplindrone")

n=int(input("enter a number: "))
palin(n)