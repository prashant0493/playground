'''Fibonacci series program in recursive way...
www.python-course.eu/python3_recursive_functions.php'''
        
def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

#definition ends here..............................

num=int(input("level for fibonacci?\n"))
for i in range(num):
    print(fibonacci(i))

