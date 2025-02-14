a,b,c,d = 10,20,30,40
def funA():
    a,b,c = 100,200,300
    print("In funA", a,b,c,d)
    def funB():
        a,b = 1000,2000
        print("In funB", a,b,c,d)
        def funC():
            a=1000
            # global b,c,d - This gives the global (b=20,c=30,d=40).
            print("In funC",a,b,c,d)
        funC()
    funB()
funA()
print("In",__name__,a,b,c,d)