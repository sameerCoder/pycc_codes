# Generator function and normal function difference.
import random
import time

name=['python','java','c','c++']

def p_list(length):
    result=[]
    for i in range(length):
        person={
            'id':i,
            'name':random.choice(name)}
        result.append(person)
    return result

def p_generator(length):
    for i in range(length):
        person={'id':i,
                'name':random.choice(name)}
        yield person
'''
t1=time.clock()# to get the current time.
people=p_list(100000)
t2=time.clock()

'''
# For running generator function 
t1=time.clock()
people=p_generator(100000000)
t2=time.clock()

print('total time took {}'.format(t2-t1))

