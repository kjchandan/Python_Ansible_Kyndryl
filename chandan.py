def divide(a,b):
    return a/b

def validate(fun):
    def nested(x,y):
        if y > x:
            x,y = y,x
        return fun(x,y)
    return nested
    
divide=validate(divide)
print(divide(10,20))
print(divide(20,10))


