def yieldfun(num):
    num=num+20
    #return num
    yield num

if __name__=="__main__":
    num=20
    num2=yieldfun(num)
    print(type(num2))
    #for i in num2:
        #print(i)
    print("outside fun:",next(num2))
