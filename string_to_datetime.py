# string to datetime.


import datetime

str1="2019/11/02"

s=datetime.datetime.strptime(str1,"%Y/%m/%d")
year=s.strftime("%Y")
print(s)
print("year:",year)
