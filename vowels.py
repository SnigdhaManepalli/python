def vowels(s):
    s=s.lower()
    k=set("aeiou")
    z=set()
    for i in s:
        if i in k:
            z.add(i)
    if len(z)==len(k):
        print('Accepted')
    else:
        print('not accepted')

s='sajjkjkj'
vowels(s)




