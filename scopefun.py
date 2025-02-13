def maxG(a,b):
    if a > b:
        return "a in global"
    return "b in global"
def funA(a,b):
    def maxA(a,b):
        if a > b:
            return "a in funA"
        return "b in funA"
    def funB(a,b):
        def maxB(a,b):
            if a > b:
                return "a in funB"
            return "b in funB"
        def funC(a,b):
            def maxC(a,b):
                if a > b:
                    return "a in funC"
                return "b in funC"
            print(max(a,b))
        funC(a,b)
    funB(a,b)
funA(10,20)