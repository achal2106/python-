#BY DEFINING FUNCTION

def fib(x):
    a,b=0,1
    while(a<=x):
        print(a,end=',')
        a,b=b,a+b
    print()

fib(10)