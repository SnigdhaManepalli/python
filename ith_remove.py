def remove(s,t):
    k=""
    for i in range(len(s)):
        if i==t:
            s=s.replace(s[i],"",1)
    print(s)


s="sniegdha"
t=int(input("Enter the value of i: "))
remove(s,t)
