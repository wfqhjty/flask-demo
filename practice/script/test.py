class Test:

    def get_return(self):
        return 1,2

if __name__=='__main__':
    test=Test()
    result=test.get_return()
    print(result)
    print (type(result))
    print(result[0])
    print(result[1])
    a,b=test.get_return()
    print("a:"+str(a)+"b:"+str(b))
