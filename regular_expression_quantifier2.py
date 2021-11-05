# Regular expression Quantifier .

'''

Qunatifiers:
How many times those character came or based on number of those character select the pattern 
p = exactly one 'p'
p+ = atleast one p 
p* = p zero or more p  .
p? = atmost one p , means zero p as well as one p only.

p{n} = Exactly n number of p
p{m,n} = minimum m number of p and maximum n number of p.

^p = means word start with p or not .
p$ = means word end with p character or not.
'''

import re

matches=re.search("p{4}","pyhtonispurehighlevelprogrammingabctppp")
print("details of pattern ",matches)
if matches:
    print("Match found - pppp , 4 continuous p got.")
    
    #for m in matches:
    print("matches are:",matches.group())
else:
    print("No 4 continuous p got.")
