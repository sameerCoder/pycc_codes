# second example of decorator .

def dec(func):

    def inner(a,b):
        if b==0:
            print("divide by zero not  possible.")
            return
        else:
            return func(a,b)
    return inner

@dec
def normaldivfun(a,b):
    return a/b

print(normaldivfun(10,2))
print(normaldivfun(12,0))

            
