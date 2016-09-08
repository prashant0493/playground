'''exercise no.6.5...from thinkpython.pdf'''
'''this is working but global variable known is getting flooded with lot of data...i don't know why'''

known={}

def ack(m,n):
    if (m,n) in known:
        return known[(m,n)]
    else:
        if m==0:
            return n+1
        if m>0 and n==0:
            return ack(m-1,1)    
        if m>0 and n>0:
            res= ack(m-1,ack(m,n-1))
            known[(m,n)]=res
            return res

m=int(input("Tell me m:"))
n=int(input("Tell me n:"))
print(ack(m,n))
print(known)

