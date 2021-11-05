# Arithmetic Bit wise Operator

#  convert each digit value to binary.

print("4 & 6 ",4 & 6 )

# 4 in binary is 100
# 6 in binary is 110
# Now mulitplication both 100 * 110 = 100 i.e 4
# 5 in binary number is 101

print("4 ^ 5 ",4^5)


####

a,b=60,2

#a in binary 0011 1100 
#b in binary 0000 0010

print("a & b",a&b)
print("a | b",a|b)# 0011 1110
print("a^b ",a^b)
#int('0b01000011',2)
'''
For 4 bit logic, you should just subtract from 0b1111

0b1111 - 0b1100 #for not operation .'''
print("~5 ",~5)
#+ve5 = 00000000..... 0101,
#0 msb means +ve number , 1 msb means -ve number.
# -ve number is represented in 2's complimentary .
# so ~5= 1111111.......1010, here msb is wat 1 means -ve value.
         #leaving msb do 1's complement and then add 1 = 2's complement.
         #100000.......0101 +1 = 1000000....0110

# left shift operator
printprint(10<<2)# 0000....1010 -- _ _ 000....1010 _ _ = 00 000....1010 0 0= 40 in decimal
print(10>>2)#0000...1010-- _ _ 000...10= 0000...10= 2 in decimal
print("a <<b ",a<<b) # binary left shift operator
print("a>>b ",a>>b) # binary right shift operator


1100<<2
#0011
1100<<2
#0000

i=10
i=i+1 # compound assignemnt , i+=1 is equal to writting i=i+1
print(i)

i*=1 #ie equal to i =i*1
print(i)

i-=1 #is equal to i=i-1
print(i)




