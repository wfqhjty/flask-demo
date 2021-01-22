class Test:

    def get_return(self):
        return 1,2

if __name__=='__main__':
    test=Test()
    result=test.get_return()
    print(result)
    print (type(result))
