# This is String Method Programe.

str1= "    hello worldz  "
str22="abcde"

print("String  1:",str1)
print("stripped string :",str1.strip())

stripstr1= str1.strip()

print("stripstr1:",stripstr1)

print("Strin1 max :",max(str1))
print("str1 min :",min(str22))


strstar="*****hello"

print("strstar",strstar)



str2= "this is string 2 "
print("String 2:",str2)

str3=str1+str2

print("unstrip string :",str3)

str4=stripstr1+str2
print("len(str1):",len(str1))
print("len(stripstr1):",len(stripstr1))
print("strip string :",str4)




# Below is for lower case .
str11="Hello World"
strstar="*****hello***"
print("lower case string :",str11.lower())

str1= "    hello worldz  "

# Below check wheather the string is in lower case or not.
print("check lower case of string ",str1.islower())


print(" Replace character :",str11.replace("H","J"))
print(" Replace character :",str11.replace("H","J").replace("W","tt"))
#print("Replace Multiple:",str1.translate(str1.maketrans({'H':'jj','W':'ttt'})))


# capitalize the sentences.
print("String2 capitalize :",str22.capitalize())

# Title
print("String2 Title:",str22.title())


#left strip.
print("string1 left string:",str1.lstrip())
print("stringstar left string:",strstar.lstrip("*"))

#print("Strin1 max :",max(str1))

print("String1 replace o with ss:",str1.replace("o","ss",1))



