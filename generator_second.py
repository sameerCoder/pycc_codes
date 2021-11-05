# generator 2 programe.

def gfunction(a,b):
    yield a+b, a-b

gyield=gfunction(10,12)
print(gyield)
print(type(gyield))
for g in gyield:
    print(g)
