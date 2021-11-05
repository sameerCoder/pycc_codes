# Assertion example 1

'''
# Simple Assertion version .

lang="python"


assert lang=="python" # if assert condition is true then only it will go down
                    # and will read the down lines of code ELSE it will give AssertionError.

print("Down line of assert lang==python")

assert lang!="python"

print("Down line of assert lang!=python")
print(lang)



#2- Argument Assertion version.

x=11
if x>5:
    print("x value is greater than 5")
    
#assert x>5 , "x>5 assert active." 
assert x <5 , "x value should be less than 5"
# Above is the assertion with argument
# if the assert condition  is false
# then Assertion Exception will generate with  msg .

print("Last msg:",x)





## Multi Assertion Argument .

x=11

assert x==11,"x value is not 11"
# if the above assert is correct then it won't print the msg and will read down code.
print("first assertion passed ")

assert x <5 , "x value should be less than 5"
# Above is the assertion with argument
# if the assert condition  is false
# then Assertion Exception will generate with  msg .
print("second assert is passed ")
print(x)

'''


# pratical use of assert .

def add1(a,b):
    print("a:",a)
    print("b:",b)
    return a+b

assert add1(3,3)==6,"The sum of a,b should be 5"
assert add1(2,-2)==0,"The sum of 2,2 should be 4"

#add1(2,3)
#add1(2,2)


'''
## Correct of above add1 .
def add1(a,b):
    return a+b

assert add1(2,3)==5,"The sum of 2,3 should be 5"
assert add1(2,2)==4,"The sum of 2,2 should be 4"

print(add1(2,3))

print(add1(2,2))

'''
