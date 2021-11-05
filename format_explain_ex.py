#Format definition & example.
#78.987889----78.98
'''

Format is a string function.
str.format()
format is use to style , design the value & way of display .
format will take unstyle value and it will return / result in as desire style value.

Syntax : { } .format(value)



Parameters :
(value) : Can be an integer, floating point
numeric constant, string, characters or even variables.

Returntype : Returns a formatted string with the value
passed as parameter in the placeholder position.

'''

print("Hi this is {} programming {}".format("python","language."))

print("Hi {mylang} is better than {secondlang}".format(mylang="python",secondlang="java"))
print("Hi {mylang} is better than {secondlang}".format(secondlang="C++",mylang="C"))
print("Hi {1} is better than {0}".format("Php","Perl"))

'''
# Type Specifying.
s – strings
d – decimal integers (base-10)
f – floating point display
c – character
b – binary
o – octal
x – hexadecimal with lowercase letters after 9
X – hexadecimal with uppercase letters after 9
e – exponent notation

Syntax :
String {field_name:conversion} Example.format(value)

Errors and Exceptions :
ValueError : Error occurs during type conversion in this method.

'''

#print("22/7 value is {0:d}".format(22/7))
print("22/7 value is {0:f}".format(22/7))
print("22/7 value is {0:.3f}".format(22/7))
print("22/7 value is {0:.2f}".format(22798.34987237))
print("22/7 normal value is {0:f} and  33/6 float 2 decimal place is: {1:.2f}".format(22/7,33/6))
print("binary of 17 is {0:b}".format(17))
print("octa of 17 is {0:0}".format(17))
print("hexa of 17 is {0:x}".format(17))

##############################
#for i in range(1,17):
 #   print("{0:2d} {1:o} {2:x} {3:b}".format(i,i,i,i))


