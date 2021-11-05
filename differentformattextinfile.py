# writing bold different format in file by python

with open("differentformattextinfile.txt","w")as diffformattext:

    diffformattext.write("""{ \b Bold \b0}\n""")
    diffformattext.write(r"\\b normal\\b0 text")
    
