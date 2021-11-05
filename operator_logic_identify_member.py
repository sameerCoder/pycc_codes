# logical operator

a,b,c,d=10,5,2,1

print("a:",a,"b:",b,"c:",c,"d:",d)



print("(a<b)and (c<d) ",(a<b)and (c<d))  # 0 * 0 

print(" (a<b)or(c<d) ",(a<b)or(c<d)) # 0 + 0 
print(" (a<b)or(c>d) ",(a<b)or(c>d))
print("not(a<b) ",not(a<b))

#exit()
### Identity operator

a,b,c=10,10,5
print("a is b",a is b)
print("a is c",a is c)
print("a is not b",a is not b)


### Membership operator .
s='abcdefg' # a boy can 

print("'a' in s :",'a' in s)
print("'z' in s:",'z' in s)
print("'f 'not in s:",'f'not in s)



# Ternary operator

x=30 if 10<20 else 40

print("x value :",x)

f=40 if 10>20 else 2 if 50 < 20 else 8 if 4<2 else 80
print("f:",f)


y=10 if 40<20 else 50 if 47<23 else 100

print("Y ",y)





















