
# Date and Time Module .

import time

second = time.time()


print ( " Number of second since 12:00 am January 1 , 1970 :" , second )

print( " The current time : ", time.ctime())

later60sec = time.time() + 60 # 60 sec means 1 minute .

print ( " 60 second later than current time :", time.ctime (later60sec ) )

#print(time.tm_year)
