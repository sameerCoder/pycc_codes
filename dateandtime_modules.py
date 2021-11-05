#Date and Time modules.

import datetime

x=datetime.datetime.now()
#day5=datetime.timedelta(days=5)
day5=datetime.timedelta(days=5,hours=2,seconds=900)
print("5day :",day5)
print("Current date with time :",x)
print("5 days ahead :",x+day5)
print("5 days before :",x-day5)



import time

print("The current time :",time.ctime())
later60sec=time.time()+60
print("later 30 sec :",later60sec)
print("30 secs from now :",time.ctime(later60sec))

#############
import time
print("The current time :",time.ctime())
#The current time :  Tue Nov 26 22:54:36 2019
t=time.localtime()
print("time.localtime()",t)
print("Current Year :",t.tm_year)
print("Current Month :",t.tm_mon)
print("Current Day:",t.tm_mday)
print("Day of the month :",t.tm_mday)
print("Day of the year :",t.tm_yday)


