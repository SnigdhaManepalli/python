def match(s1,s2):
    count=0
    s=[]
    for char in s1:
        if char in s2:
            s.append(char)
            count+=1
    print(count)
    return s

s1="snigdha"
s2="sniwqwq"
match(s1,s2)