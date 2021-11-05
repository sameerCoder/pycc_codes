# Anonymous function .

#a=2
#b=3
#c=4

add=lambda a,b,c:a+b+c
print(add(a=2,b=3,c=4))



def add1(a,b,c):
    sum1=a+b+c
    sub2=a-b-c
    return sum1,sub2
dd=add1(2,3,4)
print("this is normal function output:",dd)


'''
cube = lambda x: x*x*x  
add=lambda x,y:x+y

print(cube(7))
print(add(5,6))
'''
