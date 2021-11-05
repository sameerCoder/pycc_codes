############################3

#prog=re.compile(pattern)
#result=prog.match(string)

#is equal to 




# compile Regular Expression .

import re

file =open("abc.txt",'r')

text = file.readlines()

file.close()


# compiling the regular expression ;

keyword = re.compile(r'i ')

# searching the file content line by line :

for line in text:

  if keyword.search (line):

    print (line)
    #print(keyword)
                     
