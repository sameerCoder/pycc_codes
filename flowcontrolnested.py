# if elif else exection flow control .

num=int(input("Enter the number:"))
num2=int(input("Enter second number"))
if num==0:
    print("number1 entered is zero.")
    if num==10:
        print("num1 is 10.")

elif num==4:
    print("number1 entered is four.")
    if num2==4:
        print("Both the numbers entered is four.")
    elif num2==5:
        print("number2 is 5.")
    else:
        print("num1 is 4 but num2 is neither 4 nor 5.")
    if num2==6:
        print("num1 is 4 and num2 is 6.")
    elif num2==7:
        print("num1 is 4 and num2 is 7.")
    else:
        print("num1 is 4 but num2 is not 6 or 7.")    
elif num==5:
    print("number1 entered is five.")
    
else:
    print("number1 entered is neither zero nor four")
