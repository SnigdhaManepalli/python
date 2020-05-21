def substring(s1,s2):
    # if s2.find(s1)!=-1:
    #     print('yes')
    # else:
    #     print('no')

    if s2.count(s1)>1:
        print('yes')
    else:
        print('no')
s1="geek"
s2="geeks for geeks"
substring(s1,s2)