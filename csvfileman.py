def builddict():
    Mydict={}
    with open('us-500.csv') as foo:
        for word in foo.readline().replace('"','').split(','):
            Mydict.setdefault(word,[])

        for line in foo.readlines():
            x=line.replace('"','').split(',')[0]
            Mydict['first_name'].append(x)
        return Mydict
print(builddict())

