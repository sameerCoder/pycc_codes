#Q4- program output -
try :
		print("inside try")
		print(10/0)
		print("end of try")
except:
    print("inside except")
    print(10/2)
    try:
        b=10
        a=bin(b)
        number=int(a)
        print("end of except")
    except:
            print("Inner except block.")
print("end of program")

