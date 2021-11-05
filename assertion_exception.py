# Assertion Exception .


def sum(a,b):

  sum = a+b
  #if sum>0 : print("sum is greater than zero.")
  assert (sum>0), " Too low value i.e sum is less than zero."

  #if sum>0:
   # print("sum is greater than zero, positive sum.")

  return (sum)

a= int (input(" Enter the first number :"))

b= int (input(" Enter the second number :"))

print(sum(a,b))
