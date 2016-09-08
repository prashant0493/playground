def histogram():
    Mydict={}

    with open('try1.txt') as foo:
        for line in foo:
            word=line.split(',')
            Mydict.setdefault(word[0], word[1])
    return Mydict

Mydict1=histogram()
for person in Mydict1:
    for i in range(0,len(dict)):
        print('\t'*i+'\n'* (10-Mydict1[person]))
        print('\t'*i+'*'*Mydict1[person])
        print('\t'*i+'\n'*11+person)