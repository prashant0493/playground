known={0:0,1:1}

def fibonacci(num):
    if num in known:
        return known[num]
    res=fibonacci(num-1)+fibonacci(num-2)
    known[num]=res
    return res

#definition ends here....................

num=int(input("Level of fibonacci?\n"))
print("here you go")
for i in range(num):
    print(fibonacci(i))
