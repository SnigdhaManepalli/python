n=int(input("enter a number: "))
temp=0
even=0
odd=0
while(n!=0):
    temp=n%10
    if(temp%2==0):
        even+=1
    else:
        odd+=1
    n=n//10
print(even)
print(odd)
