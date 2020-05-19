def st_num(n):
        b=0
        if n>0:
          n=n%10
          b=b+(n**2)
        print(b)


n=int(input("enter a number: "))
st_num(n)
