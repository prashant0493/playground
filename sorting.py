def is_sorted(list1):
    i=0
    le=len(list1)-1
    while(i<le):
        if list1[i]<list1[i+1]:
            pass
        else:
            return False
        i+=1
    return True
       
L=[1,4,3] 
print(is_sorted(L))
