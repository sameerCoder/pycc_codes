# lambda function inside normal function.


def myfun(n):
    print("n:",n)
    #myfun(10) # Recursive function .
    if n==6:
        print("Bye")
        #exit()
        return 1
    
    else:
        #exit()
        #myfun(n-1)
        print("n:",n*myfun(n-1))
        return 2


    #return lambda a:a*n
    return lambda a:a*a

mydouble=myfun(12)
print(mydouble(11))

mytriple=myfun(3)
print(mytriple(11))


myfourth=myfun(4)
print(myfourth(2))


square=lambda z:z*z

print(square(12))
