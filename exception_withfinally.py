# Exceptional with finally and else.

'''
try:
    print("inside try")
    print(10/0)

except:
    print("inside except")
    

finally:
    print("inside finally.")
    print("Thank you.")
'''

try:
    print("inside try")
    print(10/0)

except:
    print("inside except")
    
else:
    print("inside else block.")

finally:
    print("inside finally.")
    print("Thank you.")


    
