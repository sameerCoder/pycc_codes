# reading a xlsc
import pandas as pd

df=pd.read_excel("pandasbook.xlsx",sheet=2,sep="\t")
# In above i am reading only the sheet 2 from excel file.

xls = pd.ExcelFile('pandasbook.xlsx',sep="\t")
# In above i am reading all the excel file containing all the sheets.
df1 = pd.read_excel(xls, 'Sheet1')
df2 = pd.read_excel(xls, 'Sheet2')

print(df2)
