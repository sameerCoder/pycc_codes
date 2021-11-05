

'''
#Code 1
try:
    10/0


except:
    print("line1 except")
    try:
        10/0
'''
'''
#Code 2
try:
    10/0


except:
    print("line1 except")
    try:
        10/0
    except:
        print("inside inner second except")
        
'''
'''
#Code 3
try:
    10/0


except:
    print("line1 except")
    try:
        10/0
    finally:
        print("finally this will execute for sure")
        
'''
'''
#Code 3
try:
    10/0


except:
    print("line1 except")
    try:
        10/2
    finally:
        print("finally this will execute for sure")
        
'''
'''
try:
    10/0


except:
    print("line1 except")
    try:
        10/2
    
    except:
        print("inside inner second except")

    else:
        print("else part below except")
'''
'''
try:
    10/0


except:
    print("line1 except")
    try:
        10/2
    
    except:
        print("inside inner second except")

    else:
        print("else part below except")

    finally:
        print("This is finally block.")

'''


try:
    10/0


except:
    print("line1 except")
    try:
        10/2
    
    except:
        print("inside inner second except")

    else:
        print("else part below except")

    finally:
        print("This is finally block.")
        10/0
        #num1=int(input("enter num:"))






        
    
